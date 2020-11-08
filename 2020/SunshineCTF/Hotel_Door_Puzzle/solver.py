import angr

p = angr.Project('hotel_key_puzzle')
main_addr = p.loader.main_object.get_symbol('main').rebased_addr
print('main_addr = ',main_addr)
state = p.factory.entry_state()
sim = p.factory.simulation_manager(state)
addr_success = main_addr + (0x22BA-0x221B)
sim.explore(find=addr_success)
if len(sim.found) > 0:
    print(sim.found[0].posix.dumps(0))