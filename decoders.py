import string

alphabet = list(string.ascii_lowercase)
# print(alphabet)
# offset = 14

msg = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'

def decoding(msg, offset):
  alpha_offset = {alphabet[i-offset] if i - offset >= 0 else alphabet[i-offset+len(alphabet)]: alphabet[i]  for i in range(0, len(alphabet)) }
  new_msg = [alpha_offset[i] if i in alpha_offset.keys() else i for i in msg]
  decoded = ''
  for i in new_msg:
    decoded = decoded + str(i)
  print(decoded)

msg_to_encode = 'Hey there, my hands are writting. I am studing and doing my best everyday to become a Data Analyst.'

def encoding(msg_to_encode, offset):
  alpha_onset = {alphabet[i+offset] if i + offset < len(alphabet) else alphabet[i+offset-len(alphabet)]: alphabet[i]  for i in range(0, len(alphabet)) }
  encoded = ''
  for i in msg_to_encode:
    letter = alpha_onset[i.lower() ] if i in alpha_onset.keys() else i
    encoded = encoded + letter
  print(encoded)

# Task 2
# decoding('jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.', 10)
# decoding('bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!', 14)

# msg = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

# Task 4
# for i in range(0, len(alphabet)):
  # decoding(msg, i)

## Task 5 - Decoder vignere Cipher ---------------------------------------
dict_vig = {alphabet[i]:i for i in range(0, len(alphabet))}
dict_vig_rev = {x:y for x, y in list(zip(dict_vig.values(), dict_vig.keys()))}

msg = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"           
keyword = "friends"
                
# Translate msg to numeric values
def msg_to_num(msg):
  msg_to_num = [dict_vig[i.lower()] if i.lower() in dict_vig.keys() else i for i in msg]
  # print(msg_to_num)
  return msg_to_num

# Convert numbers to letters
def num_to_letters(msg):
  msg_decoded = ''
  for i in msg:
    if not isinstance(i, int):
      msg_decoded += i
    else:
      msg_decoded += dict_vig_rev[i]
  print(msg_decoded)
  return msg_decoded

def vig_decoder(msg, keyword):
  # Sumar valores:
  a = msg_to_num(msg)
  b = msg_to_num(keyword)
  result = []
  space_count = 0

  for i in range(0, len(msg)):
    # Verifica si no es número
    if not isinstance(a[i], int) or not isinstance(b[i % len(b)], int):
      result.append(a[i])
      space_count += 1

    else:
      x = int(a[i]) + int(b[(i - space_count)% len(b)])
      result.append(x % len(dict_vig_rev))
  
  return num_to_letters(result)


# vig_decoder(msg, keyword)


# # Task 6 - Encoder vignere Cipher-------------------------------------
msg = 'On my way to become a Data Analyst!'
keyword = 'python'

def vig_encoder(msg, keyword):
  a = msg_to_num(msg)
  b = msg_to_num(keyword)

  # New numbers
  result = []
  space_count = 0
  for i in range(0, len(msg)):
    # Verifica si no es número
    if not isinstance(a[i], int) or not isinstance(b[i % len(b)], int):
      result.append(a[i])
      space_count += 1
    else:
      x = int(a[i]) - int(b[(i - space_count)% len(b)])
      result.append(x % len(dict_vig_rev))

  # print(result)
  return num_to_letters(result)


# Test ---------------------------
test = vig_encoder(msg, keyword)
vig_decoder(test, keyword)