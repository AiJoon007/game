
default lun_ev_talk_to_me_t1_e1 = Event(id="lun_ev_talk_to_me_t1_e1", label="ll_pf_talk_T1_E1_intro", req="states.lun.tier == 1", queue="lun_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False, repeat=False)
default lun_ev_talk_to_me_t1_e2 = Event(id="lun_ev_talk_to_me_t1_e2", label="ll_pf_talk_T1_E2_intro", req="states.lun.tier == 1", queue="lun_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False, repeat=False)
default lun_ev_talk_to_me_t1_e3 = Event(id="lun_ev_talk_to_me_t1_e3", label="ll_pf_talk_T1_E3_intro", req="states.lun.tier == 1", queue="lun_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False, repeat=False)
default lun_ev_talk_to_me_t1_e4 = Event(id="lun_ev_talk_to_me_t1_e4", label="ll_pf_talk_T1_E4_repeat", req="states.lun.tier == 1", queue="lun_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False)
default lun_ev_talk_to_me_t2_e1 = Event(id="lun_ev_talk_to_me_t2_e1", label="ll_pf_talk_T2_E1_repeat", req="states.lun.tier == 2", queue="lun_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False)
default lun_ev_talk_to_me_t3_e1 = Event(id="lun_ev_talk_to_me_t3_e1", label="ll_pf_talk_T3_E1_repeat", req="states.lun.tier >= 3", queue="lun_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False)

default lun_ev_inspect_her_body_t2_e1 = Event(id="lun_ev_inspect_her_body_t2_e1", label="ll_pf_inspect_T2_E1_intro", req="states.lun.tier == 2", queue="lun_eventqueue_inspect_her_body", autoenqueue=True, autodequeue=False, repeat=False)
default lun_ev_inspect_her_body_t2_e2 = Event(id="lun_ev_inspect_her_body_t2_e2", label="ll_pf_inspect_T2_E2_intro", req="states.lun.tier == 2", queue="lun_eventqueue_inspect_her_body", autoenqueue=True, autodequeue=False, repeat=False)
default lun_ev_inspect_her_body_t2_e3 = Event(id="lun_ev_inspect_her_body_t2_e3", label="ll_pf_inspect_T2_E3_intro", req="states.lun.tier == 2", queue="lun_eventqueue_inspect_her_body", autoenqueue=True, autodequeue=False, repeat=False)
default lun_ev_inspect_her_body_t2_e4 = Event(id="lun_ev_inspect_her_body_t2_e4", label="ll_pf_inspect_T2_E4_repeat", req="states.lun.tier == 2", queue="lun_eventqueue_inspect_her_body", autoenqueue=True, autodequeue=False)
default lun_ev_inspect_her_body_t3_e1 = Event(id="lun_ev_inspect_her_body_t3_e1", label="ll_pf_inspect_T3_E1_repeat", req="states.lun.tier >= 3", queue="lun_eventqueue_inspect_her_body", autoenqueue=True, autodequeue=False)

default lun_ev_play_with_yourself_t3_e1 = Event(id="lun_ev_play_with_yourself_t3_e1", label="ll_pf_masturbate_T3_E1_intro", req="states.lun.tier >= 3", queue="lun_eventqueue_play_with_yourself", autoenqueue=True, autodequeue=False, repeat=False)
default lun_ev_play_with_yourself_t3_e2 = Event(id="lun_ev_play_with_yourself_t3_e2", label="ll_pf_masturbate_T3_E2_intro", req="states.lun.tier >= 3", queue="lun_eventqueue_play_with_yourself", autoenqueue=True, autodequeue=False, repeat=False)
default lun_ev_play_with_yourself_t3_e3 = Event(id="lun_ev_play_with_yourself_t3_e3", label="ll_pf_masturbate_T3_E3_intro", req="states.lun.tier >= 3", queue="lun_eventqueue_play_with_yourself", autoenqueue=True, autodequeue=False, repeat=False)
default lun_ev_play_with_yourself_t3_e4 = Event(id="lun_ev_play_with_yourself_t3_e4", label="ll_pf_masturbate_T3_E4_repeat", req="states.lun.tier >= 3", queue="lun_eventqueue_play_with_yourself", autoenqueue=True, autodequeue=False)

define luna_favors = [
    ("lun_eventqueue_talk_to_me", "Talk to me!"),
    ("lun_eventqueue_inspect_her_body", "Let me inspect you!"),
    ("lun_eventqueue_play_with_yourself", "Play with yourself!"),
]