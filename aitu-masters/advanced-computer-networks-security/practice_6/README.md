# practice-6

Forked and modified BGP hijack demo from Mininet wiki for Mininet 2.3.0
- https://github.com/mininet/mininet/wiki/BGP-Path-Hijacking-Attack-Demo
- https://bitbucket.org/jvimal/bgp/src/
- https://github.com/spwpun/BGP_Path_Hijack
- https://github.com/humberto-ortiz/BGP_Path_Hijack

Requirements installation:
```
sudo apt update
sudo apt install frr \
                 mininet \
                 openvswitch-testcontroller
```
- or build frr from source: https://docs.frrouting.org/projects/dev-guide/en/latest/building-frr-for-ubuntu2004.html
- frr (FRRouting) need for GNU Zebra and Quagga BGP
- Removed "termcolor"
- Then turn off and disable the openvswitch controller
TODO: https://stackoverflow.com/questions/21687357/mininet-ovs-controller-can-t-be-loaded-and-run
```
$ sudo systemctl stop openvswitch-testcontroller
$ sudo systemctl disable openvswitch-testcontroller
```
