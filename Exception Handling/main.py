"""write specific exceptions at top and general exceptions at bottom because only one
 exception will run """
from logging import exception

try:
    file=open("test.txt","r")
    text=file.read()
    file.close()
    # raising own exception , now this will be thrown at exception as e block
    if file.name=="test.txt":
        raise exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
#else block will run only if no exception is thrown
else:
    print("Else block executed")
finally:
    print("Alhamdulillah")