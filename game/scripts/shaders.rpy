init python:
    renpy.register_shader("outline_shader", fragment_300="""
        const float THICKNESS = 1.0 / 128.0;
        vec4 col = texture2D(tex0, v_tex_coord);

        if (col.a <= 0.5) {
            float a = texture2D(tex0, vec2(v_tex_coord.x + THICKNESS, v_tex_coord.y)).a +
            texture2D(tex0, vec2(v_tex_coord.x, v_tex_coord.y - THICKNESS)).a +
            texture2D(tex0, vec2(v_tex_coord.x - THICKNESS, v_tex_coord.y)).a +
            texture2D(tex0, vec2(v_tex_coord.x, v_tex_coord.y + THICKNESS)).a;

            if (col.a < 1.0 && a > 0.0)
                gl_FragColor = vec4(0.0, 1.0, 0.0, 0.8);
            else
                gl_FragColor = col;
        }
    """)

    renpy.register_shader("color_temperature_shader", variables="""
            uniform float u_factor;
            uniform float u_strength;
        """, fragment_functions="""
            vec3 ctemp2rgb(float ctemp) {
                mat3 m = (ctemp <= 6500.0) ? mat3(vec3(0.0, -2902.1955373783176, -8257.7997278925690),
                                                vec3(0.0, 1669.5803561666639, 2575.2827530017594),
                                                vec3(1.0, 1.3302673723350029, 1.8993753891711275)) :
                                                mat3(vec3(1745.0425298314172, 1216.6168361476490, -8257.7997278925690),
                                                vec3(-2666.3474220535695, -2173.1012343082230, 2575.2827530017594),
                                                vec3(0.55995389139931482, 0.70381203140554553, 1.8993753891711275));
                return mix(clamp(vec3(m[0] / (vec3(clamp(ctemp, 1000.0, 40000.0)) + m[1]) + m[2]), vec3(0.0), vec3(1.0)), vec3(1.0), smoothstep(1000.0, 0.0, ctemp));
            }
        """, fragment_300="""
        float ctemp = mix(1000.0, 40000.0, u_factor);
        gl_FragColor = vec4(mix(gl_FragColor.xyz, gl_FragColor.xyz * ctemp2rgb(ctemp), u_strength), 1.0);
    """)

transform color_temperature(factor=1.0, strength=1.0):
    mesh True
    shader "color_temperature_shader"

    u_factor factor # 0.075 dusk, 0.1 dawn, 0.5 evening, 1.0 night
    u_strength strength
