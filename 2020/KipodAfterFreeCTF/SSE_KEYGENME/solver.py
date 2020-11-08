import angr

p = angr.Project('SSE_KEYGENME')
main_addr = p.loader.main_object.get_symbol('main').rebased_addr
print('main_addr = ',main_addr)
state = p.factory.entry_state()
sim = p.factory.simulation_manager(state)
addr_success = main_addr + (0xD48-0xC6D)
# addr_failed = main_addr + (0xD4F-0xC6D)
sim.explore(find=addr_success)
if len(sim.found) > 0:
    print(sim.found[0].posix.dumps(0))