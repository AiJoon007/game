
default her_ev_talk_to_me_t1_e1 = Event(id="her_ev_talk_to_me_t1_e1", label="hg_pf_talk_T1_intro_E1", priority=5, req="states.her.tier == 1", queue="her_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["end_hg_pf_talk"])
default her_ev_talk_to_me_t1_e2 = Event(id="her_ev_talk_to_me_t1_e2", label="hg_pf_talk_T1_E1", priority=6, req="states.her.tier == 1", queue="her_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False, ignore_labels=["end_hg_pf_talk"])
default her_ev_talk_to_me_t2_e1 = Event(id="her_ev_talk_to_me_t2_e1", label="hg_pf_talk_T2_intro_E1", priority=5, req="states.her.tier == 2", queue="her_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["end_hg_pf_talk"])
default her_ev_talk_to_me_t2_e2 = Event(id="her_ev_talk_to_me_t2_e2", label="hg_pf_talk_T2_E1", priority=6, req="states.her.tier == 2", queue="her_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False, ignore_labels=["end_hg_pf_talk"])
default her_ev_talk_to_me_t3_e1 = Event(id="her_ev_talk_to_me_t3_e1", label="hg_pf_talk_T3_intro_E1", priority=5, req="states.her.tier >= 3", queue="her_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["end_hg_pf_talk", "hg_pf_talk_tonks_T3_intro_E1", "hg_pf_talk_tonks_T3_E1"])
default her_ev_talk_to_me_t3_e2 = Event(id="her_ev_talk_to_me_t3_e2", label="hg_pf_talk_T3_intro_E2", priority=6, req="states.her.tier >= 3", queue="her_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["end_hg_pf_talk", "hg_pf_talk_tonks_T3_intro_E1", "hg_pf_talk_tonks_T3_E1"])
default her_ev_talk_to_me_t3_e3 = Event(id="her_ev_talk_to_me_t3_e3", label="hg_pf_talk_T3_repeat", priority=7, req="states.her.tier >= 3", queue="her_eventqueue_talk_to_me", autoenqueue=True, autodequeue=False, ignore_labels=["end_hg_pf_talk", "hg_pf_talk_tonks_T3_intro_E1", "hg_pf_talk_tonks_T3_E1"])

default her_ev_talk_to_me_tonks_t3_e1 = Event(id="her_ev_talk_to_me_tonks_t3_e1", label="hg_pf_talk_tonks_T3_intro_E1", priority=5, req="states.her.tier >= 3", queue="her_eventqueue_talk_to_me_tonks", autoenqueue=True, autodequeue=False, repeat=False)
default her_ev_talk_to_me_tonks_t3_e2 = Event(id="her_ev_talk_to_me_tonks_t3_e2", label="hg_pf_talk_tonks_T3_E1", priority=6, req="states.her.tier >= 3", queue="her_eventqueue_talk_to_me_tonks", autoenqueue=True, autodequeue=False)

default her_ev_admire_panties_t1_e1 = Event(id="her_ev_admire_panties_t1_e1", label="hg_pf_admire_panties_T1_intro_E1", priority=5, req="states.her.tier == 1", queue="her_eventqueue_admire_panties", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["end_hg_pf_admire_panties"])
default her_ev_admire_panties_t1_e2 = Event(id="her_ev_admire_panties_t1_e2", label="hg_pf_admire_panties_T1_E1", priority=6, req="states.her.tier == 1", queue="her_eventqueue_admire_panties", autoenqueue=True, autodequeue=False, ignore_labels=["end_hg_pf_admire_panties"])
default her_ev_admire_panties_t2_e1 = Event(id="her_ev_admire_panties_t2_e1", label="hg_pf_admire_panties_T2_intro_E1", priority=5, req="states.her.tier == 2", queue="her_eventqueue_admire_panties", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["end_hg_pf_admire_panties"])
default her_ev_admire_panties_t2_e2 = Event(id="her_ev_admire_panties_t2_e2", label="hg_pf_admire_panties_T2_E1", priority=6, req="states.her.tier == 2", queue="her_eventqueue_admire_panties", autoenqueue=True, autodequeue=False, ignore_labels=["end_hg_pf_admire_panties"])
default her_ev_admire_panties_t3_e1 = Event(id="her_ev_admire_panties_t3_e1", label="hg_pf_admire_panties_T3_intro_E1", priority=5, req="states.her.tier == 3", queue="her_eventqueue_admire_panties", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["end_hg_pf_admire_panties"])
default her_ev_admire_panties_t3_e2 = Event(id="her_ev_admire_panties_t3_e2", label="hg_pf_admire_panties_T3_E1", priority=6, req="states.her.tier == 3", queue="her_eventqueue_admire_panties", autoenqueue=True, autodequeue=False, ignore_labels=["end_hg_pf_admire_panties"])
default her_ev_admire_panties_t4_e1 = Event(id="her_ev_admire_panties_t4_e1", label="hg_pf_admire_panties_T4_intro_E1", priority=5, req="states.her.tier >= 4", queue="her_eventqueue_admire_panties", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["end_hg_pf_admire_panties"])
default her_ev_admire_panties_t4_e2 = Event(id="her_ev_admire_panties_t4_e2", label="hg_pf_admire_panties_T4_E1", priority=6, req="states.her.tier >= 4", queue="her_eventqueue_admire_panties", autoenqueue=True, autodequeue=False, ignore_labels=["end_hg_pf_admire_panties"])
default her_ev_admire_panties_t4_e3 = Event(id="her_ev_admire_panties_t4_e3", label="hg_pf_admire_panties_T4_E2", priority=7, req="states.her.tier >= 4", queue="her_eventqueue_admire_panties", autoenqueue=True, autodequeue=False, ignore_labels=["end_hg_pf_admire_panties"])

default her_ev_admire_breasts_t1_e1 = Event(id="her_ev_admire_breasts_t1_e1", label="hg_pf_admire_breasts_T1_intro_E1", priority=5, req="states.her.tier == 1", queue="her_eventqueue_admire_breasts", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["end_hg_pf_admire_breasts"])
default her_ev_admire_breasts_t1_e2 = Event(id="her_ev_admire_breasts_t1_e2", label="hg_pf_admire_breasts_T1_intro_E2", priority=6, req="states.her.tier == 1", queue="her_eventqueue_admire_breasts", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["end_hg_pf_admire_breasts"])
default her_ev_admire_breasts_t1_e3 = Event(id="her_ev_admire_breasts_t1_e3", label="hg_pf_admire_breasts_T1_E2", priority=7, req="states.her.tier == 1", queue="her_eventqueue_admire_breasts", autoenqueue=True, autodequeue=False, ignore_labels=["end_hg_pf_admire_breasts"])
default her_ev_admire_breasts_t2_e1 = Event(id="her_ev_admire_breasts_t2_e1", label="hg_pf_admire_breasts_T2_intro_E1", priority=5, req="states.her.tier == 2", queue="her_eventqueue_admire_breasts", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["end_hg_pf_admire_breasts", "hg_pf_admire_breasts_T2", "hg_pf_admire_breasts_T2_masturbate"])
default her_ev_admire_breasts_t2_e2 = Event(id="her_ev_admire_breasts_t2_e2", label="hg_pf_admire_breasts_T2_intro_E2", priority=6, req="states.her.tier == 2", queue="her_eventqueue_admire_breasts", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["end_hg_pf_admire_breasts", "hg_pf_admire_breasts_T2", "hg_pf_admire_breasts_T2_masturbate"])
default her_ev_admire_breasts_t2_e3 = Event(id="her_ev_admire_breasts_t2_e3", label="hg_pf_admire_breasts_T2_E2", priority=7, req="states.her.tier == 2", queue="her_eventqueue_admire_breasts", autoenqueue=True, autodequeue=False, ignore_labels=["end_hg_pf_admire_breasts", "hg_pf_admire_breasts_T2", "hg_pf_admire_breasts_T2_masturbate"])
default her_ev_admire_breasts_t3_e1 = Event(id="her_ev_admire_breasts_t3_e1", label="hg_pf_admire_breasts_T3_intro_E1", priority=5, req="states.her.tier == 3", queue="her_eventqueue_admire_breasts", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["end_hg_pf_admire_breasts", "hg_pf_admire_breasts_T3"])
default her_ev_admire_breasts_t3_e2 = Event(id="her_ev_admire_breasts_t3_e2", label="hg_pf_admire_breasts_T3_E1", priority=6, req="states.her.tier == 3", queue="her_eventqueue_admire_breasts", autoenqueue=True, autodequeue=False, ignore_labels=["end_hg_pf_admire_breasts", "hg_pf_admire_breasts_T3"])
default her_ev_admire_breasts_t4_e1 = Event(id="her_ev_admire_breasts_t4_e1", label="hg_pf_admire_breasts_T4_intro_E1", priority=5, req="states.her.tier >= 4", queue="her_eventqueue_admire_breasts", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["end_hg_pf_admire_breasts", "hg_pf_admire_breasts_T4"])
default her_ev_admire_breasts_t4_e2 = Event(id="her_ev_admire_breasts_t4_e2", label="hg_pf_admire_breasts_T4_E1", priority=6, req="states.her.tier >= 4", queue="her_eventqueue_admire_breasts", autoenqueue=True, autodequeue=False, ignore_labels=["end_hg_pf_admire_breasts", "hg_pf_admire_breasts_T4"])
default her_ev_admire_breasts_t4_e3 = Event(id="her_ev_admire_breasts_t4_e3", label="hg_pf_admire_breasts_T4_E2", priority=7, req="states.her.tier >= 4", queue="her_eventqueue_admire_breasts", autoenqueue=True, autodequeue=False, ignore_labels=["end_hg_pf_admire_breasts", "hg_pf_admire_breasts_T4"])

default her_ev_grope_t1_e1 = Event(id="her_ev_grope_t1_e1", label="hg_pf_grope_T1_E1", priority=5, req="states.her.tier == 1", queue="her_eventqueue_grope", autoenqueue=True, autodequeue=False)
default her_ev_grope_t2_e1 = Event(id="her_ev_grope_t2_e1", label="hg_pf_grope_T2_intro_E1", priority=5, req="states.her.tier == 2", queue="her_eventqueue_grope", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["hg_pf_grope_breasts_T2", "hg_pf_grope_ass_T2", "hg_pf_grope_ass_T2_back", "hg_pf_grope_ass_T2_front", "hg_pf_grope_ass_T2_continue", "hg_pf_grope_breasts_T2_continue"])
default her_ev_grope_t2_e2 = Event(id="her_ev_grope_t2_e2", label="hg_pf_grope_T2_E1", priority=6, req="states.her.tier == 2", queue="her_eventqueue_grope", autoenqueue=True, autodequeue=False, ignore_labels=["hg_pf_grope_breasts_T2", "hg_pf_grope_ass_T2", "hg_pf_grope_ass_T2_back", "hg_pf_grope_ass_T2_front", "hg_pf_grope_ass_T2_continue", "hg_pf_grope_breasts_T2_continue"])
default her_ev_grope_t3_e1 = Event(id="her_ev_grope_t3_e1", label="hg_pf_grope_T3_intro_E1", priority=5, req="states.her.tier == 3", queue="her_eventqueue_grope", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["hg_pf_grope_breasts_T3", "hg_pf_grope_ass_T3", "hg_pf_grope_ass_T3_back", "hg_pf_grope_ass_T3_front", "hg_pf_grope_ass_T3_continue", "hg_pf_grope_breasts_T3_continue"])
default her_ev_grope_t3_e2 = Event(id="her_ev_grope_t3_e2", label="hg_pf_grope_T3_E1", priority=6, req="states.her.tier == 3", queue="her_eventqueue_grope", autoenqueue=True, autodequeue=False, ignore_labels=["hg_pf_grope_breasts_T3", "hg_pf_grope_ass_T3", "hg_pf_grope_ass_T3_back", "hg_pf_grope_ass_T3_front", "hg_pf_grope_ass_T3_continue", "hg_pf_grope_breasts_T3_continue"])
default her_ev_grope_t4_e1 = Event(id="her_ev_grope_t4_e1", label="hg_pf_grope_T4_intro_E1", priority=5, req="states.her.tier >= 4", queue="her_eventqueue_grope", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["hg_pf_grope_breasts_T4", "hg_pf_grope_ass_T4", "hg_pf_grope_ass_T4_back", "hg_pf_grope_ass_T4_front", "hg_pf_grope_ass_T4_continue", "hg_pf_grope_breasts_T4_continue"])
default her_ev_grope_t4_e2 = Event(id="her_ev_grope_t4_e2", label="hg_pf_grope_T4_intro_E2", priority=6, req="states.her.tier >= 4", queue="her_eventqueue_grope", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["hg_pf_grope_breasts_T4", "hg_pf_grope_ass_T4", "hg_pf_grope_ass_T4_back", "hg_pf_grope_ass_T4_front", "hg_pf_grope_ass_T4_continue", "hg_pf_grope_breasts_T4_continue"])
default her_ev_grope_t4_e3 = Event(id="her_ev_grope_t4_e3", label="hg_pf_grope_T4_E2", priority=7, req="states.her.tier >= 4", queue="her_eventqueue_grope", autoenqueue=True, autodequeue=False, ignore_labels=["hg_pf_grope_breasts_T4", "hg_pf_grope_ass_T4", "hg_pf_grope_ass_T4_back", "hg_pf_grope_ass_T4_front", "hg_pf_grope_ass_T4_continue", "hg_pf_grope_breasts_T4_continue"])

default her_ev_strip_for_me_t1_e1 = Event(id="her_ev_strip_for_me_t1_e1", label="hg_pf_strip_T1_E1", priority=5, req="states.her.tier == 1", queue="her_eventqueue_strip_for_me", autoenqueue=True, autodequeue=False)
default her_ev_strip_for_me_t2_e1 = Event(id="her_ev_strip_for_me_t2_e1", label="hg_pf_strip_T2_E1", priority=5, req="states.her.tier == 2", queue="her_eventqueue_strip_for_me", autoenqueue=True, autodequeue=False)
default her_ev_strip_for_me_t3_e1 = Event(id="her_ev_strip_for_me_t3_e1", label="hg_pf_strip_T3_intro_E1", priority=5, req="states.her.tier == 3", queue="her_eventqueue_strip_for_me", autoenqueue=True, autodequeue=False, repeat=False)
default her_ev_strip_for_me_t3_e2 = Event(id="her_ev_strip_for_me_t3_e2", label="hg_pf_strip_T3_intro_E2", priority=6, req="states.her.tier == 3", queue="her_eventqueue_strip_for_me", autoenqueue=True, autodequeue=False, repeat=False)
default her_ev_strip_for_me_t3_e3 = Event(id="her_ev_strip_for_me_t3_e3", label="hg_pf_strip_T3_E2", priority=7, req="states.her.tier == 3", queue="her_eventqueue_strip_for_me", autoenqueue=True, autodequeue=False, ignore_labels=["hg_pf_strip_T3_masturbate", "hg_pf_strip_T3_watch", "hg_pf_strip_T3_snape"])
default her_ev_strip_for_me_t4_e1 = Event(id="her_ev_strip_for_me_t4_e1", label="hg_pf_strip_T4_intro_E1", priority=5, req="states.her.tier >= 4", queue="her_eventqueue_strip_for_me", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["hg_pf_strip_T4", "hg_pf_strip_T4_snape", "hg_pf_strip_T4_masturbate", "hg_pf_strip_T4_watch", "hg_pf_strip_T4_fingering", "hg_pf_strip_T5_fingering", "hg_pf_strip_T6_fingering"])
default her_ev_strip_for_me_t4_e2 = Event(id="her_ev_strip_for_me_t4_e2", label="hg_pf_strip_T4_intro_E2", priority=6, req="states.her.tier >= 4", queue="her_eventqueue_strip_for_me", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["hg_pf_strip_T4", "hg_pf_strip_T4_snape", "hg_pf_strip_T4_masturbate", "hg_pf_strip_T4_watch", "hg_pf_strip_T4_fingering", "hg_pf_strip_T5_fingering", "hg_pf_strip_T6_fingering"])
default her_ev_strip_for_me_t4_e3 = Event(id="her_ev_strip_for_me_t4_e3", label="hg_pf_strip_T4_E2", priority=7, req="states.her.tier >= 4", queue="her_eventqueue_strip_for_me", autoenqueue=True, autodequeue=False, ignore_labels=["hg_pf_strip_T4", "hg_pf_strip_T4_snape", "hg_pf_strip_T4_masturbate", "hg_pf_strip_T4_watch", "hg_pf_strip_T4_fingering", "hg_pf_strip_T5_fingering", "hg_pf_strip_T6_fingering"])

default her_ev_handjob_t1_e1 = Event(id="her_ev_handjob_t1_e1", label="hg_pf_handjob_T1_E1", priority=5, req="states.her.tier == 1", queue="her_eventqueue_handjob", autoenqueue=True, autodequeue=False)
default her_ev_handjob_t2_e1 = Event(id="her_ev_handjob_t2_e1", label="hg_pf_handjob_T2_E1", priority=5, req="states.her.tier == 2", queue="her_eventqueue_handjob", autoenqueue=True, autodequeue=False)
default her_ev_handjob_t3_e1 = Event(id="her_ev_handjob_t3_e1", label="hg_pf_handjob_T3_E1", priority=5, req="states.her.tier == 3", queue="her_eventqueue_handjob", autoenqueue=True, autodequeue=False)
default her_ev_handjob_t4_e1 = Event(id="her_ev_handjob_t4_e1", label="hg_pf_handjob_T4_intro_E1", priority=5, req="states.her.tier == 4", queue="her_eventqueue_handjob", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["hg_pf_handjob_1"])
default her_ev_handjob_t4_e2 = Event(id="her_ev_handjob_t4_e2", label="hg_pf_handjob_T4_intro_E2", priority=6, req="states.her.tier == 4", queue="her_eventqueue_handjob", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["hg_pf_handjob_1"])
default her_ev_handjob_t4_e3 = Event(id="her_ev_handjob_t4_e3", label="hg_pf_handjob_T4_repeat", priority=7, req="states.her.tier == 4", queue="her_eventqueue_handjob", autoenqueue=True, autodequeue=False, ignore_labels=["hg_pf_handjob_1"])
default her_ev_handjob_t5_e1 = Event(id="her_ev_handjob_t5_e1", label="hg_pf_handjob_T5_intro_E1", priority=5, req="states.her.tier >= 5", queue="her_eventqueue_handjob", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["hg_pf_handjob_2", "hg_pf_handjob_2_cumming", "hg_pf_handjob_2_continue"])
default her_ev_handjob_t5_e2 = Event(id="her_ev_handjob_t5_e2", label="hg_pf_handjob_T5_intro_E2", priority=6, req="states.her.tier >= 5", queue="her_eventqueue_handjob", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["hg_pf_handjob_2", "hg_pf_handjob_2_cumming", "hg_pf_handjob_2_continue"])
default her_ev_handjob_t5_e3 = Event(id="her_ev_handjob_t5_e3", label="hg_pf_handjob_T5_repeat", priority=7, req="states.her.tier >= 5", queue="her_eventqueue_handjob", autoenqueue=True, autodequeue=False, ignore_labels=["hg_pf_handjob_2", "hg_pf_handjob_2_cumming", "hg_pf_handjob_2_continue"])

default her_ev_titjob_t1_e1 = Event(id="her_ev_titjob_t1_e1", label="hg_pf_titjob_T1_E1", priority=5, req="states.her.tier == 1", queue="her_eventqueue_titjob", autoenqueue=True, autodequeue=False)
default her_ev_titjob_t2_e1 = Event(id="her_ev_titjob_t2_e1", label="hg_pf_titjob_T2_E1", priority=5, req="states.her.tier == 2", queue="her_eventqueue_titjob", autoenqueue=True, autodequeue=False)
default her_ev_titjob_t3_e1 = Event(id="her_ev_titjob_t3_e1", label="hg_pf_titjob_T3_E1", priority=5, req="states.her.tier == 3", queue="her_eventqueue_titjob", autoenqueue=True, autodequeue=False)
default her_ev_titjob_t4_e1 = Event(id="her_ev_titjob_t4_e1", label="hg_pf_titjob_T4_E1", priority=5, req="states.her.tier == 4", queue="her_eventqueue_titjob", autoenqueue=True, autodequeue=False)
default her_ev_titjob_t5_e1 = Event(id="her_ev_titjob_t5_e1", label="hg_pf_titjob_T5_intro_E1", priority=5, req="states.her.tier == 5", queue="her_eventqueue_titjob", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["back_to_titjob_choices", "hg_pf_titjob_1"])
default her_ev_titjob_t5_e2 = Event(id="her_ev_titjob_t5_e2", label="hg_pf_titjob_T5_repeat", priority=6, req="states.her.tier == 5", queue="her_eventqueue_titjob", autoenqueue=True, autodequeue=False, ignore_labels=["hg_pf_titjob_1"])
default her_ev_titjob_t6_e1 = Event(id="her_ev_titjob_t6_e1", label="hg_pf_titjob_T6_intro_E1", priority=5, req="states.her.tier >= 6", queue="her_eventqueue_titjob", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["hg_pf_titjob_2", "hg_pf_titjob_2_cumming", "hg_pf_titjob_2_continue"])
default her_ev_titjob_t6_e2 = Event(id="her_ev_titjob_t6_e2", label="hg_pf_titjob_T6_intro_E2", priority=6, req="states.her.tier >= 6", queue="her_eventqueue_titjob", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["hg_pf_titjob_2", "hg_pf_titjob_2_cumming", "hg_pf_titjob_2_continue"])
default her_ev_titjob_t6_e3 = Event(id="her_ev_titjob_t6_e3", label="hg_pf_titjob_T6_repeat", priority=7, req="states.her.tier >= 6", queue="her_eventqueue_titjob", autoenqueue=True, autodequeue=False, ignore_labels=["hg_pf_titjob_2", "hg_pf_titjob_2_cumming", "hg_pf_titjob_2_continue"])

default her_ev_blowjob_t1_e1 = Event(id="her_ev_blowjob_t1_e1", label="hg_pf_blowjob_T1_E1", priority=5, req="states.her.tier == 1", queue="her_eventqueue_blowjob", autoenqueue=True, autodequeue=False)
default her_ev_blowjob_t2_e1 = Event(id="her_ev_blowjob_t2_e1", label="hg_pf_blowjob_T2_E1", priority=5, req="states.her.tier == 2", queue="her_eventqueue_blowjob", autoenqueue=True, autodequeue=False)
default her_ev_blowjob_t3_e1 = Event(id="her_ev_blowjob_t3_e1", label="hg_pf_blowjob_T3_E1", priority=5, req="states.her.tier == 3", queue="her_eventqueue_blowjob", autoenqueue=True, autodequeue=False)
default her_ev_blowjob_t4_e1 = Event(id="her_ev_blowjob_t4_e1", label="hg_pf_blowjob_T4_E1", priority=5, req="states.her.tier == 4", queue="her_eventqueue_blowjob", autoenqueue=True, autodequeue=False)
default her_ev_blowjob_t5_e1 = Event(id="her_ev_blowjob_t5_e1", label="hg_pf_blowjob_T5_intro_E1", priority=5, req="states.her.tier == 5", queue="her_eventqueue_blowjob", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["hg_pf_blowjob_1", "hg_pf_blowjob_2", "hg_pf_hidden_blowjob", "hg_hidden_blowjob_snape", "hg_hidden_blowjob_tonks", "hg_hidden_blowjob_luna", "hg_hidden_blowjob_cumming"])
default her_ev_blowjob_t5_e2 = Event(id="her_ev_blowjob_t5_e2", label="hg_pf_blowjob_T5_intro_E2", priority=6, req="states.her.tier == 5", queue="her_eventqueue_blowjob", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["hg_pf_blowjob_1", "hg_pf_blowjob_2", "hg_pf_hidden_blowjob", "hg_hidden_blowjob_snape", "hg_hidden_blowjob_tonks", "hg_hidden_blowjob_luna", "hg_hidden_blowjob_cumming"])
default her_ev_blowjob_t5_e3 = Event(id="her_ev_blowjob_t5_e3", label="hg_pf_blowjob_T5_repeat", priority=7, req="states.her.tier == 5", queue="her_eventqueue_blowjob", autoenqueue=True, autodequeue=False, ignore_labels=["hg_pf_blowjob_1", "hg_pf_blowjob_2", "hg_pf_hidden_blowjob", "hg_hidden_blowjob_snape", "hg_hidden_blowjob_tonks", "hg_hidden_blowjob_luna", "hg_hidden_blowjob_cumming"])
default her_ev_blowjob_t6_e1 = Event(id="her_ev_blowjob_t6_e1", label="hg_pf_blowjob_T6_intro_E1", priority=5, req="states.her.tier >= 6", queue="her_eventqueue_blowjob", autoenqueue=True, autodequeue=False, repeat=False, ignore_labels=["hg_pf_blowjob_1", "hg_pf_blowjob_2", "hg_pf_hidden_blowjob", "hg_hidden_blowjob_snape", "hg_hidden_blowjob_tonks", "hg_hidden_blowjob_luna", "hg_hidden_blowjob_cumming"])
default her_ev_blowjob_t6_e2 = Event(id="her_ev_blowjob_t6_e2", label="hg_pf_blowjob_T6_hidden_repeat", priority=6, req="states.her.tier >= 6", queue="her_eventqueue_blowjob", autoenqueue=True, autodequeue=False, ignore_labels=["hg_pf_blowjob_1", "hg_pf_blowjob_2", "hg_pf_hidden_blowjob", "hg_hidden_blowjob_snape", "hg_hidden_blowjob_tonks", "hg_hidden_blowjob_luna", "hg_hidden_blowjob_cumming"])
default her_ev_blowjob_t6_e3 = Event(id="her_ev_blowjob_t6_e3", label="hg_pf_blowjob_T6_repeat", priority=7, req="states.her.tier >= 6", queue="her_eventqueue_blowjob", autoenqueue=True, autodequeue=False, ignore_labels=["hg_pf_blowjob_1", "hg_pf_blowjob_2", "hg_pf_hidden_blowjob", "hg_hidden_blowjob_snape", "hg_hidden_blowjob_tonks", "hg_hidden_blowjob_luna", "hg_hidden_blowjob_cumming"])

default her_ev_sex_t1_e1 = Event(id="her_ev_sex_t1_e1", label="hg_pf_sex_T1_E1", priority=5, req="states.her.tier == 1", queue="her_eventqueue_sex", autoenqueue=True, autodequeue=False)
default her_ev_sex_t2_e1 = Event(id="her_ev_sex_t2_e1", label="hg_pf_sex_T2_E1", priority=5, req="states.her.tier == 2", queue="her_eventqueue_sex", autoenqueue=True, autodequeue=False)
default her_ev_sex_t3_e1 = Event(id="her_ev_sex_t3_e1", label="hg_pf_sex_T3_E1", priority=5, req="states.her.tier == 3", queue="her_eventqueue_sex", autoenqueue=True, autodequeue=False)
default her_ev_sex_t4_e1 = Event(id="her_ev_sex_t4_e1", label="hg_pf_sex_T4_E1", priority=5, req="states.her.tier == 4", queue="her_eventqueue_sex", autoenqueue=True, autodequeue=False)
default her_ev_sex_t5_e1 = Event(id="her_ev_sex_t5_e1", label="hg_pf_sex_T5_E1", priority=5, req="states.her.tier == 5", queue="her_eventqueue_sex", autoenqueue=True, autodequeue=False)
default her_ev_sex_t6_e1 = Event(id="her_ev_sex_t6_e1", label="hg_pf_sex_T6_intro_E1", priority=5, req="states.her.tier >= 6", queue="her_eventqueue_sex", autoenqueue=True, autodequeue=False, repeat=False)
default her_ev_sex_t6_e2 = Event(id="her_ev_sex_t6_e2", label="hg_pf_sex_T6_intro_E2", priority=6, req="states.her.tier >= 6", queue="her_eventqueue_sex", autoenqueue=True, autodequeue=False, repeat=False)
default her_ev_sex_t6_e3 = Event(id="her_ev_sex_t6_e3", label="hg_pf_sex_T6_intro_E3", priority=7, req="states.her.tier >= 6", queue="her_eventqueue_sex", autoenqueue=True, autodequeue=False, repeat=False)
default her_ev_sex_t6_e4 = Event(id="her_ev_sex_t6_e4", label="hg_pf_sex_T6_E3", priority=8, req="states.her.tier >= 6", queue="her_eventqueue_sex", autoenqueue=True, autodequeue=False)

default her_ev_anal_t6_e1 = Event(id="her_ev_anal_t6_e1", label="hg_anal_sex_1_intro", priority=5, req="states.her.tier >= 6", queue="her_eventqueue_anal", autoenqueue=True, autodequeue=False, repeat=False)
default her_ev_anal_t6_e2 = Event(id="her_ev_anal_t6_e2", label="hg_anal_sex_2_intro", priority=6, req="states.her.tier >= 6", queue="her_eventqueue_anal", autoenqueue=True, autodequeue=False, repeat=False)
default her_ev_anal_t6_e3 = Event(id="her_ev_anal_t6_e3", label="hg_anal_sex_3", priority=7, req="states.her.tier >= 6", queue="her_eventqueue_anal", autoenqueue=True, autodequeue=False)

define hermione_favors = [
    ("her_eventqueue_talk_to_me", "Talk to me!"), 
    ("her_eventqueue_admire_breasts", "Show me your tits!"), 
    ("her_eventqueue_admire_panties", "Show me your panties!"), 
    ("her_eventqueue_grope", "Grope her!"), 
    ("her_eventqueue_strip_for_me", "Strip for me!"),
    ("her_eventqueue_handjob", "Give me a handy!"),
    ("her_eventqueue_titjob", "Give me a tittyjob!"),
    ("her_eventqueue_blowjob", "Suck it!"),
    ("her_eventqueue_sex", "Let's have sex!"),
    ]
