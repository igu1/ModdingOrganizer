# if mod_id_uc.strip('') == '' and name_uc.strip('') == '':
#     print('INVALID MOD ID AND NAME')
# elif mod_id_uc.strip('') == '':
#     print('INVALID MOD ID!')
# elif name_uc.strip('') == '':
#     print('INVALID MOD NAME!')
# else:
#     all_attributes.append(mod_id_uc)
#     all_attributes.append(name_uc)
#     try:
#         # str(dir_p[0])
#         if str(dir_p[0]).strip('\n ') == '' or dir_p == '[]':
#             print('INVALID MOD DIR PATH')
#             try:
#                 if str(logo_p[0]).strip('') == '':
#                     all_attributes.append('Example.png')
#                 else:
#                     all_attributes.append(str(logo_p[0]))
#             except IndexError:
#                 all_attributes.append('Example.png')
#                 print('Example PNG SELECTED')
#             except:
#                 pass
#         else:
#             try:
#                 all_attributes.append(str(logo_p[0]))
#                 all_attributes.append(str(dir_p[0]))
#                 print(all_attributes)
#                 if all_attributes[0] != '' or all_attributes[1] != '' or all_attributes[2] != '' or all_attributes[3] != '':
#                     work(mod_id_uc, name_uc, str(all_attributes[2]), str(all_attributes[3]))
#                 else:
#                     print("EveryThing Must Be Filled!!")
#                     pass
#             except IndexError:
#                 print("EveryThing Must Be Filled!!11111111")
#                 pass
#     except IndexError:
#         print('INVALID MOD DIR PATH')