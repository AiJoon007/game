
default ton_ev_detention_t1_e1 = Event(id="ton_ev_detention_t1_e1", label="nt_pr_teach_T1_E1", req="game.daytime==False")
default ton_ev_detention_t1_e2 = Event(id="ton_ev_detention_t1_e2", label="nt_pr_teach_T1_E2", req="game.daytime==False")
default ton_ev_detention_t1_e3 = Event(id="ton_ev_detention_t1_e3", label="nt_pr_teach_T1_E3", req="game.daytime==False")
default ton_ev_detention_t1_e4 = Event(id="ton_ev_detention_t1_e4", label="nt_pr_teach_T1_E4", req="game.daytime==False")

default ton_ev_detention_t1_e1_hub = Event(id="ton_ev_detention_t1_e1_hub", label="nt_pr_teach_start", req="states.ton.tier==1", autoenqueue=True, autodequeue=False, queue="ton_eventqueue_detention", subevents=["ton_ev_detention_t1_e1"])
default ton_ev_detention_t1_e2_hub = Event(id="ton_ev_detention_t1_e2_hub", label="nt_pr_teach_start", req="states.ton.tier==1", autoenqueue=True, autodequeue=False, queue="ton_eventqueue_detention", subevents=["ton_ev_detention_t1_e2"])
default ton_ev_detention_t1_e3_hub = Event(id="ton_ev_detention_t1_e3_hub", label="nt_pr_teach_start", req="states.ton.tier==1", autoenqueue=True, autodequeue=False, queue="ton_eventqueue_detention", subevents=["ton_ev_detention_t1_e3"])
default ton_ev_detention_t1_e4_hub = Event(id="ton_ev_detention_t1_e4_hub", label="nt_pr_teach_start", req="states.ton.tier==1", autoenqueue=True, autodequeue=False, queue="ton_eventqueue_detention", subevents=["ton_ev_detention_t1_e4"])

default ton_ev_detention_t2_e1 = Event(id="ton_ev_detention_t2_e1", label="nt_pr_teach_T2_E1", req="game.daytime==False")
default ton_ev_detention_t2_e2 = Event(id="ton_ev_detention_t2_e2", label="nt_pr_teach_T2_E2", req="game.daytime==False")
default ton_ev_detention_t2_e3 = Event(id="ton_ev_detention_t2_e3", label="nt_pr_teach_T2_E3", req="game.daytime==False")
default ton_ev_detention_t2_e4 = Event(id="ton_ev_detention_t2_e4", label="nt_pr_teach_T2_E4", req="game.daytime==False")

default ton_ev_detention_t2_e1_hub = Event(id="ton_ev_detention_t2_e1_hub", label="nt_pr_teach_start", req="states.ton.tier>=2", autoenqueue=True, autodequeue=False, queue="ton_eventqueue_detention", subevents=["ton_ev_detention_t2_e1"])
default ton_ev_detention_t2_e2_hub = Event(id="ton_ev_detention_t2_e2_hub", label="nt_pr_teach_start", req="states.ton.tier>=2", autoenqueue=True, autodequeue=False, queue="ton_eventqueue_detention", subevents=["ton_ev_detention_t2_e2"])
default ton_ev_detention_t2_e3_hub = Event(id="ton_ev_detention_t2_e3_hub", label="nt_pr_teach_start", req="states.ton.tier>=2", autoenqueue=True, autodequeue=False, queue="ton_eventqueue_detention", subevents=["ton_ev_detention_t2_e3"])
default ton_ev_detention_t2_e4_hub = Event(id="ton_ev_detention_t2_e4_hub", label="nt_pr_teach_start", req="states.ton.tier>=2", autoenqueue=True, autodequeue=False, queue="ton_eventqueue_detention", subevents=["ton_ev_detention_t2_e4"])

default ton_ev_grope_t2_e1 = Event(id="ton_ev_grope_t2_e1", label="nt_pr_grope_T2_E1", req="game.daytime==False")
default ton_ev_grope_t2_e2 = Event(id="ton_ev_grope_t2_e2", label="nt_pr_grope_T2_E2", req="game.daytime==False")
default ton_ev_grope_t2_e3 = Event(id="ton_ev_grope_t2_e3", label="nt_pr_grope_T2_E3", req="game.daytime==False")
default ton_ev_grope_t2_e4 = Event(id="ton_ev_grope_t2_e4", label="nt_pr_grope_T2_E4", req="game.daytime==False")

default ton_ev_grope_t2_e1_hub = Event(id="ton_ev_grope_t2_e1_hub", label="nt_pr_grope_start", req="states.ton.tier>=2", autoenqueue=True, autodequeue=False, queue="ton_eventqueue_grope", subevents=["ton_ev_grope_t2_e1"])
default ton_ev_grope_t2_e2_hub = Event(id="ton_ev_grope_t2_e2_hub", label="nt_pr_grope_start", req="states.ton.tier>=2", autoenqueue=True, autodequeue=False, queue="ton_eventqueue_grope", subevents=["ton_ev_grope_t2_e2"])
default ton_ev_grope_t2_e3_hub = Event(id="ton_ev_grope_t2_e3_hub", label="nt_pr_grope_start", req="states.ton.tier>=2", autoenqueue=True, autodequeue=False, queue="ton_eventqueue_grope", subevents=["ton_ev_grope_t2_e3"])
default ton_ev_grope_t2_e4_hub = Event(id="ton_ev_grope_t2_e4_hub", label="nt_pr_grope_start", req="states.ton.tier>=2", autoenqueue=True, autodequeue=False, queue="ton_eventqueue_grope", subevents=["ton_ev_grope_t2_e4"])

default ton_ev_oral_t2_e1 = Event(id="ton_ev_oral_t2_e1", label="nt_pr_kiss_T2_intro_E1", req="game.daytime==False")
default ton_ev_oral_t2_e2 = Event(id="ton_ev_oral_t2_e2", label="nt_pr_kiss_T2_E2", req="game.daytime==False")
default ton_ev_oral_t2_e3 = Event(id="ton_ev_oral_t2_e3", label="nt_pr_kiss_T2_E3", req="game.daytime==False")
default ton_ev_oral_t2_e4 = Event(id="ton_ev_oral_t2_e4", label="nt_pr_kiss_T2_E4", req="game.daytime==False")

default ton_ev_oral_t2_e1_hub = Event(id="ton_ev_oral_t2_e1_hub", label="nt_pr_kiss_start", req="states.ton.tier>=2", repeat=False, autoenqueue=True, autodequeue=False, queue="ton_eventqueue_oral", subevents=["ton_ev_oral_t2_e1"])
default ton_ev_oral_t2_e2_hub = Event(id="ton_ev_oral_t2_e2_hub", label="nt_pr_kiss_start", req="states.ton.tier>=2", autoenqueue=True, autodequeue=False, queue="ton_eventqueue_oral", subevents=["ton_ev_oral_t2_e2"])
default ton_ev_oral_t2_e3_hub = Event(id="ton_ev_oral_t2_e3_hub", label="nt_pr_kiss_start", req="states.ton.tier>=2", autoenqueue=True, autodequeue=False, queue="ton_eventqueue_oral", subevents=["ton_ev_oral_t2_e3"])
default ton_ev_oral_t2_e4_hub = Event(id="ton_ev_oral_t2_e4_hub", label="nt_pr_kiss_start", req="states.ton.tier>=2", autoenqueue=True, autodequeue=False, queue="ton_eventqueue_oral", subevents=["ton_ev_oral_t2_e4"])

define tonks_requests = [
    ("ton_eventqueue_detention", "Detention with Tonks!"),
    ("ton_eventqueue_grope", "Hands-on lessons!"),
    ("ton_eventqueue_oral", "Oral practice!"),
]

# Idea for "blowjob pr" name: "Stress Mitigation."