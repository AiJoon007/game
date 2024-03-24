init offset = 5

default her_ev_maid_job_return = Event(id="her_ev_maid_job_return", label="her_maid_job_return", priority=5, req="not game.daytime")
default her_ev_maid_job_hub = Event(id="her_ev_maid_job_hub", label="her_maid_job", priority=5, req="her_outfit_maid.unlocked", repeat=True, autoenqueue=True, autodequeue=False, queue="her_eventqueue_jobs_maid", subevents=["her_ev_maid_job_return"])

default her_ev_promoter_job_return = Event(id="her_ev_promoter_job_return", label="her_promoter_job_return", priority=5, req="not game.daytime")
default her_ev_promoter_job_hub = Event(id="her_ev_promoter_job_hub", label="her_promoter_job", priority=5, req="states.her.ev.promote_cardgame.offered and poker_outfit_ITEM.unlocked", repeat=True, autoenqueue=True, autodequeue=False, queue="her_eventqueue_jobs_promoter", subevents=["her_ev_promoter_job_return"])


default her_ev_panty_thief_t1_e1 = Event(id="her_ev_panty_thief_t1_e1", label="hg_pr_panty_thief_T1_E1", req="states.her.tier == 1", autoenqueue=True, autodequeue=False, queue="her_eventqueue_panty_thief")
default her_ev_panty_thief_t2_e1 = Event(id="her_ev_panty_thief_t2_e1", label="hg_pr_panty_thief_T2_E1", req="states.her.tier == 2", autoenqueue=True, autodequeue=False, queue="her_eventqueue_panty_thief")
default her_ev_panty_thief_t3_e1 = Event(id="her_ev_panty_thief_t3_e1", label="hg_pr_panty_thief_e1_return", req="game.daytime==False")
default her_ev_panty_thief_t3_e1_hub = Event(id="her_ev_panty_thief_t3_e1_hub", label="hg_pr_panty_thief_e1", req="states.her.tier >= 3", autoenqueue=True, autodequeue=False, queue="her_eventqueue_panty_thief", subevents=["her_ev_panty_thief_t3_e1"])

define hermione_jobs = [
    ("her_eventqueue_jobs_maid", "Work as a maid!"),
    ("her_eventqueue_jobs_promoter", "Work as a promoter!"),
    ("her_eventqueue_panty_thief", "Ditch the panties!"),
]
