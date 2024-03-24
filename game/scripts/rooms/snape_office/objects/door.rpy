
label snape_office_door:

    if not states.map.snape_office.intro_e2:
        gen "(I have to finish snooping around before leaving.)" ("base", xpos="far_left", ypos="head")
    else:
        jump return_office

    jump snape_office_menu
