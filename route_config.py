#!/usr/bin/env python

import subprocess, socket, struct, os

vmnetiface_prefix = 'vmnet'
laniface_prefix = 'en'
wlaniface_prefix = 'wlan'
vpniface_prefix = 'utun'
vpnips = ['10']

def _run_command(cmd, mute=False):
    if not mute:
        print cmd

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        raise Exception('Command:\n%s\nreturn %d' % (cmd, retcode))

    if not mute:
        print output

    return output

def debug_run_command(cmd, mute=False):
    if mute:
        return _run_command('sudo ' + cmd, mute)
    else:
        print cmd

run_command = _run_command

def getifaces():
    ifaces = {}
    out = run_command('ifconfig', mute=True)
    iface = ''
    for line in out.splitlines():
        if line.startswith('\t'):
            if line.strip().startswith('inet '):
                ippart, maskpart = line.split('netmask')
                ip = ippart.split()[1]
                mask = maskpart.split()[0]
                ifaces[iface] = (ip, mask)
        else:
            iface = line.split(':')[0]
    return ifaces

def get_infos(ifaces, prefix):
    ret = []
    for key, value in ifaces.iteritems():
        if key.startswith(prefix):
            ret.append((key, value))
    return ret

def config_for_vmnet(ifaces):
    infos = get_infos(ifaces, vmnetiface_prefix)
    for iface, info in infos:
        ip, mask = info
        ip = ip.rsplit('.', 1)[0]  # FIXME: handle mask here
        run_command('route change -net %s -interface %s' % (ip, iface))

def config_for_vpn(ifaces):
    infos = get_infos(ifaces, vpniface_prefix)
    if infos:
        vpn_iface = infos[0][0]
        for vpnip in vpnips:
            run_command('route add -net %s -interface %s' % (vpnip, vpn_iface))

def config_for_lan(ifaces):
    infos = get_infos(ifaces, laniface_prefix)
    if not infos:
        infos = get_infos(ifaces, wlaniface_prefix)

    for iface, info in infos:
        ip, mask = info
        ip = ip.rsplit('.', 1)[0]  # FIXME: handle mask here
        run_command('route change -net %s -interface %s' % (ip, iface))

def config_for_gateway(ifaces):
    infos = get_infos(ifaces, laniface_prefix)
    if not infos:
        infos = get_infos(ifaces, wlaniface_prefix)
    if infos:
        iface = infos[0][0]
        out = run_command('netstat -rn | grep default | grep %s' % iface, mute=True)
        gateway = out.split()[1]
        try:
            socket.inet_aton(gateway)
            run_command('route change default %s' % gateway)
        except:
            pass
    else:
        print 'network is not connected.'

def config_route(ifaces):
    config_for_vpn(ifaces)
    config_for_vmnet(ifaces)
    config_for_lan(ifaces)
    config_for_gateway(ifaces)
    run_command('route add -net %s -interface %s' % ('66.116.126', 'utun0'))

def get_cisco_last_rule_number():
    # FIXME: how to get last cisco fw rule number correctly
    out = run_command('ipfw list', mute=True)
    rules = map(lambda l:int(l.split()[0]), out.splitlines())
    i = 1
    while i in rules:
        i += 1
    i -= 1
    return i

def config_firewall(ifaces):
    infos = get_infos(ifaces, vpniface_prefix)
    if infos:
        vpn_iface = infos[0][0]
        rule = get_cisco_last_rule_number()
        run_command('ipfw delete %s' % rule)
        run_command('ipfw add %s deny ip from any to any via %s' % (rule, vpn_iface))

def main():
    ifaces = getifaces()
    if get_infos(ifaces, vpniface_prefix):  # run only vpn is up
        config_route(ifaces)
        config_firewall(ifaces)

if __name__ == '__main__':
    if os.geteuid() == 0:
        main()
    else:
        print 'root required!'
