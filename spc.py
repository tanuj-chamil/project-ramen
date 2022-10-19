def is_flag_on(byte, position):
    return bool((byte & (1<<position)) >> position)



with open('test.spc','rb') as file:
    raw_data = file.read()

    header_block = raw_data[:512]

    parameters = {}

    sub_block = header_block[0]
    parameters['y_16bit'] = is_flag_on(sub_block,0)        
    parameters['not_spc'] = is_flag_on(sub_block,1)    # use experiment extension (not .spc)
    parameters['multifile'] = is_flag_on(sub_block,2)                          
    parameters['z_random'] = is_flag_on(sub_block,3) & parameters['multifile']
    parameters['z_uneven'] = is_flag_on(sub_block,4) & parameters['multifile']
    parameters['custom_ax'] = is_flag_on(sub_block,5)
    parameters['xy_file'] = is_flag_on(sub_block,7)
    parameters['seperate_x'] = is_flag_on(sub_block,6)
    
    sub_block = header_block[1]
    if sub_block == 0x4B :
        parameters['version'] = 'new'
    elif sub_block == 0x4D :
        parameters['version'] = 'old'
    else :
        parameters['version'] = 'unknown'
    
    sub_block = header_block[2]
    parameters['exp_code'] = sub_block

    sub_block


    print(parameters)