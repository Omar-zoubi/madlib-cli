import re
print('''Welcome to Madlib Game
      You should provide some answer and then we will put them in a sentance, you cant know the sentence before you answer
      BE CARFULL''' )
def reading_file(path):

    try:
      with open(path, 'r') as file:
       new_file= file.read()
       return new_file
    except FileNotFoundError:
      raise FileNotFoundError('404 file not found')
    except:
       print("Some thing happend")

        

def filter_template(value):
    rgx = r"{(.*?)}"
    needed_value= re.findall(rgx, value)
    return needed_value
def inp_user():
    print("Plz answer these Q: ")
    qCounter=1
    userAnsewrs = []
    for i in needed_value:
        # vv = input(f"Plz Give a {i}:")
        userAnsewrs.append(input(f"Q{qCounter} Plz Give a {i}: "))
        qCounter+=1

    return userAnsewrs
   

def save_to_anew(result):
    with open("madlib_cli/newfile.txt", "w") as file:
        file.write(result)

def merge(wfile, user_answer):
    needed_value=filter_template(wfile)
    i = 0
    for x in user_answer:
        wfile = wfile.replace(needed_value[i], x , 1)
        i+=1
    wfile = wfile.replace("{" , "")
    show_value = wfile.replace("}" , "")
 
    print(show_value)

    return show_value 



if __name__ == "__main__":
    file_to_open = reading_file('madlib_cli/template.txt')
    getting_values = filter_template(file_to_open)
    user_answer = getting_values[0]
    needed_value = getting_values[1] 
    merge(file_to_open, user_answer)
    save_to_anew(merge(file_to_open, user_answer))