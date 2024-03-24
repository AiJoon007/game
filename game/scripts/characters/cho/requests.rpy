
default cho_ev_spy_on_boys_t3_e1 = Event(id="cho_ev_spy_on_boys_t3_e1", label="cc_pr_spy_boys_T3_twins", req="game.daytime==False")
default cho_ev_spy_on_boys_t3_e2 = Event(id="cho_ev_spy_on_boys_t3_e2", label="cc_pr_spy_boys_T3_ron", req="game.daytime==False")
default cho_ev_spy_on_boys_t3_e3 = Event(id="cho_ev_spy_on_boys_t3_e3", label="cc_pr_spy_boys_T3_harry", req="game.daytime==False")

default cho_ev_spy_on_boys_t3_e1_hub = Event(id="cho_ev_spy_on_boys_t3_e1_hub", label="cc_pr_spy_boys_start", req="states.cho.tier == 3", queue="cho_eventqueue_spy_on_boys", autoenqueue=True, autodequeue=False, subevents=["cho_ev_spy_on_boys_t3_e1"])
default cho_ev_spy_on_boys_t3_e2_hub = Event(id="cho_ev_spy_on_boys_t3_e2_hub", label="cc_pr_spy_boys_start", req="states.cho.tier == 3", queue="cho_eventqueue_spy_on_boys", autoenqueue=True, autodequeue=False, subevents=["cho_ev_spy_on_boys_t3_e2"])
default cho_ev_spy_on_boys_t3_e3_hub = Event(id="cho_ev_spy_on_boys_t3_e3_hub", label="cc_pr_spy_boys_start", req="states.cho.tier == 3", queue="cho_eventqueue_spy_on_boys", autoenqueue=True, autodequeue=False, subevents=["cho_ev_spy_on_boys_t3_e3"])

default cho_ev_spy_on_girls_t3_e1 = Event(id="cho_ev_spy_on_girls_t3_e1", label="cc_pr_spy_girls_T3_showers", req="game.daytime==False")
default cho_ev_spy_on_girls_t3_e2 = Event(id="cho_ev_spy_on_girls_t3_e2", label="cc_pr_spy_girls_T3_alicia", req="game.daytime==False")
default cho_ev_spy_on_girls_t3_e3 = Event(id="cho_ev_spy_on_girls_t3_e3", label="cc_pr_spy_girls_T3_katie", req="game.daytime==False")
default cho_ev_spy_on_girls_t3_e4 = Event(id="cho_ev_spy_on_girls_t3_e4", label="cc_pr_spy_girls_T3_angelina", req="game.daytime==False")

default cho_ev_spy_on_girls_t3_e1_hub = Event(id="cho_ev_spy_on_girls_t3_e1_hub", label="cc_pr_spy_girls_start", req="states.cho.tier == 3", queue="cho_eventqueue_spy_on_girls", autoenqueue=True, autodequeue=False, subevents=["cho_ev_spy_on_girls_t3_e1"])
default cho_ev_spy_on_girls_t3_e2_hub = Event(id="cho_ev_spy_on_girls_t3_e2_hub", label="cc_pr_spy_girls_start", req="states.cho.tier == 3", queue="cho_eventqueue_spy_on_girls", autoenqueue=True, autodequeue=False, subevents=["cho_ev_spy_on_girls_t3_e2"])
default cho_ev_spy_on_girls_t3_e3_hub = Event(id="cho_ev_spy_on_girls_t3_e3_hub", label="cc_pr_spy_girls_start", req="states.cho.tier == 3", queue="cho_eventqueue_spy_on_girls", autoenqueue=True, autodequeue=False, subevents=["cho_ev_spy_on_girls_t3_e3"])
default cho_ev_spy_on_girls_t3_e4_hub = Event(id="cho_ev_spy_on_girls_t3_e4_hub", label="cc_pr_spy_girls_start", req="states.cho.tier == 3", queue="cho_eventqueue_spy_on_girls", autoenqueue=True, autodequeue=False, subevents=["cho_ev_spy_on_girls_t3_e4"])

default cho_ev_manipulate_boys_t1_e1 = Event(id="cho_ev_manipulate_boys_t1_e1", label="cc_pr_manipulate_boys_T1_intro_E1", req="game.daytime==False", repeat=False)
default cho_ev_manipulate_boys_t1_e2 = Event(id="cho_ev_manipulate_boys_t1_e2", label="cc_pr_manipulate_boys_T1_E1", req="game.daytime==False")
default cho_ev_manipulate_boys_t1_e3 = Event(id="cho_ev_manipulate_boys_t1_e3", label="cc_pr_manipulate_boys_T1_E2", req="game.daytime==False")
default cho_ev_manipulate_boys_t1_e4 = Event(id="cho_ev_manipulate_boys_t1_e4", label="cc_pr_manipulate_boys_T1_E3", req="game.daytime==False")
default cho_ev_manipulate_boys_t2_e1 = Event(id="cho_ev_manipulate_boys_t2_e1", label="cc_pr_manipulate_boys_T2_intro_E1", req="game.daytime==False", repeat=False)
default cho_ev_manipulate_boys_t2_e2 = Event(id="cho_ev_manipulate_boys_t2_e2", label="cc_pr_manipulate_boys_T2_E1", req="game.daytime==False")
default cho_ev_manipulate_boys_t2_e3 = Event(id="cho_ev_manipulate_boys_t2_e3", label="cc_pr_manipulate_boys_T2_intro_E2", req="game.daytime==False", repeat=False)
default cho_ev_manipulate_boys_t2_e4 = Event(id="cho_ev_manipulate_boys_t2_e4", label="cc_pr_manipulate_boys_T2_intro_E3", req="game.daytime==False", repeat=False)
default cho_ev_manipulate_boys_t2_e5 = Event(id="cho_ev_manipulate_boys_t2_e5", label="cc_pr_manipulate_boys_T2_E3", req="game.daytime==False")
default cho_ev_manipulate_boys_t3_e1 = Event(id="cho_ev_manipulate_boys_t3_e1", label="cc_pr_manipulate_boys_T3_twins", req="game.daytime==False")
default cho_ev_manipulate_boys_t3_e2 = Event(id="cho_ev_manipulate_boys_t3_e2", label="cc_pr_manipulate_boys_T3_ron", req="game.daytime==False")
default cho_ev_manipulate_boys_t3_e3 = Event(id="cho_ev_manipulate_boys_t3_e3", label="cc_pr_manipulate_boys_T3_harry", req="game.daytime==False")

default cho_ev_manipulate_boys_t1_e1_hub = Event(id="cho_ev_manipulate_boys_t1_e1_hub", label="cc_pr_manipulate_boys_start", req="states.cho.tier == 1", queue="cho_eventqueue_manipulate_boys", autoenqueue=True, autodequeue=False, subevents=["cho_ev_manipulate_boys_t1_e1"])
default cho_ev_manipulate_boys_t1_e2_hub = Event(id="cho_ev_manipulate_boys_t1_e2_hub", label="cc_pr_manipulate_boys_start", req="states.cho.tier == 1", queue="cho_eventqueue_manipulate_boys", autoenqueue=True, autodequeue=False, subevents=["cho_ev_manipulate_boys_t1_e2"])
default cho_ev_manipulate_boys_t1_e3_hub = Event(id="cho_ev_manipulate_boys_t1_e3_hub", label="cc_pr_manipulate_boys_start", req="states.cho.tier == 1", queue="cho_eventqueue_manipulate_boys", autoenqueue=True, autodequeue=False, subevents=["cho_ev_manipulate_boys_t1_e3"])
default cho_ev_manipulate_boys_t1_e4_hub = Event(id="cho_ev_manipulate_boys_t1_e4_hub", label="cc_pr_manipulate_boys_start", req="states.cho.tier == 1", queue="cho_eventqueue_manipulate_boys", autoenqueue=True, autodequeue=False, subevents=["cho_ev_manipulate_boys_t1_e4"])
default cho_ev_manipulate_boys_t2_e1_hub = Event(id="cho_ev_manipulate_boys_t2_e1_hub", label="cc_pr_manipulate_boys_start", req="states.cho.tier == 2", queue="cho_eventqueue_manipulate_boys", autoenqueue=True, autodequeue=False, subevents=["cho_ev_manipulate_boys_t2_e1"])
default cho_ev_manipulate_boys_t2_e2_hub = Event(id="cho_ev_manipulate_boys_t2_e2_hub", label="cc_pr_manipulate_boys_start", req="states.cho.tier == 2", queue="cho_eventqueue_manipulate_boys", autoenqueue=True, autodequeue=False, subevents=["cho_ev_manipulate_boys_t2_e2"])
default cho_ev_manipulate_boys_t2_e3_hub = Event(id="cho_ev_manipulate_boys_t2_e3_hub", label="cc_pr_manipulate_boys_start", req="states.cho.tier == 2", queue="cho_eventqueue_manipulate_boys", autoenqueue=True, autodequeue=False, subevents=["cho_ev_manipulate_boys_t2_e3"])
default cho_ev_manipulate_boys_t2_e4_hub = Event(id="cho_ev_manipulate_boys_t2_e4_hub", label="cc_pr_manipulate_boys_start", req="states.cho.tier == 2", queue="cho_eventqueue_manipulate_boys", autoenqueue=True, autodequeue=False, subevents=["cho_ev_manipulate_boys_t2_e4"])
default cho_ev_manipulate_boys_t2_e5_hub = Event(id="cho_ev_manipulate_boys_t2_e5_hub", label="cc_pr_manipulate_boys_start", req="states.cho.tier == 2", queue="cho_eventqueue_manipulate_boys", autoenqueue=True, autodequeue=False, subevents=["cho_ev_manipulate_boys_t2_e5"])
default cho_ev_manipulate_boys_t3_e1_hub = Event(id="cho_ev_manipulate_boys_t3_e1_hub", label="cc_pr_manipulate_boys_start", req="states.cho.tier == 3", queue="cho_eventqueue_manipulate_boys", autoenqueue=True, autodequeue=False, subevents=["cho_ev_manipulate_boys_t3_e1"])
default cho_ev_manipulate_boys_t3_e2_hub = Event(id="cho_ev_manipulate_boys_t3_e2_hub", label="cc_pr_manipulate_boys_start", req="states.cho.tier == 3", queue="cho_eventqueue_manipulate_boys", autoenqueue=True, autodequeue=False, subevents=["cho_ev_manipulate_boys_t3_e2"])
default cho_ev_manipulate_boys_t3_e3_hub = Event(id="cho_ev_manipulate_boys_t3_e3_hub", label="cc_pr_manipulate_boys_start", req="states.cho.tier == 3", queue="cho_eventqueue_manipulate_boys", autoenqueue=True, autodequeue=False, subevents=["cho_ev_manipulate_boys_t3_e3"])

default cho_ev_manipulate_girls_t3_e1 = Event(id="cho_ev_manipulate_girls_t3_e1", label="cc_pr_manipulate_girls_T3_alicia", req="game.daytime==False")
default cho_ev_manipulate_girls_t3_e2 = Event(id="cho_ev_manipulate_girls_t3_e2", label="cc_pr_manipulate_girls_T3_katie_part1", req="game.daytime==False")
default cho_ev_manipulate_girls_t3_e3 = Event(id="cho_ev_manipulate_girls_t3_e3", label="cc_pr_manipulate_girls_T3_katie_part2", req="game.daytime==False")
default cho_ev_manipulate_girls_t3_e4 = Event(id="cho_ev_manipulate_girls_t3_e4", label="cc_pr_manipulate_girls_T3_angelina", req="game.daytime==False")

default cho_ev_manipulate_girls_t3_e1_hub = Event(id="cho_ev_manipulate_girls_t3_e1_hub", label="cc_pr_manipulate_girls_start", req="states.cho.tier == 3", queue="cho_eventqueue_manipulate_girls", autoenqueue=True, autodequeue=False, subevents=["cho_ev_manipulate_girls_t3_e1"])
default cho_ev_manipulate_girls_t3_e2_hub = Event(id="cho_ev_manipulate_girls_t3_e2_hub", label="cc_pr_manipulate_girls_start", req="states.cho.tier == 3", queue="cho_eventqueue_manipulate_girls", autoenqueue=True, autodequeue=False, subevents=["cho_ev_manipulate_girls_t3_e2"])
default cho_ev_manipulate_girls_t3_e3_hub = Event(id="cho_ev_manipulate_girls_t3_e3_hub", label="cc_pr_manipulate_girls_start", req="states.cho.tier == 3", queue="cho_eventqueue_manipulate_girls", autoenqueue=True, autodequeue=False, subevents=["cho_ev_manipulate_girls_t3_e3"])
default cho_ev_manipulate_girls_t3_e4_hub = Event(id="cho_ev_manipulate_girls_t3_e4_hub", label="cc_pr_manipulate_girls_start", req="states.cho.tier == 3", queue="cho_eventqueue_manipulate_girls", autoenqueue=True, autodequeue=False, subevents=["cho_ev_manipulate_girls_t3_e4"])

define cho_requests = [
    ("cho_eventqueue_spy_on_boys", "Spy on the boys!"),
    ("cho_eventqueue_spy_on_girls", "Spy on the girls!"),
    ("cho_eventqueue_manipulate_boys", "Manipulate the boys!"),
    ("cho_eventqueue_manipulate_girls", "Manipulate the girls!"),
]
