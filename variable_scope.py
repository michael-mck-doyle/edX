

glob = 3

print("glob" in globals())


def fun():
    loc = 2
    print(glob)
    print("loc" in globals())
    print("loc" in locals())

fun()


def shout(name):
    loud_name = name.upper()
    return loud_name


action = shout("wilma")
print(action)


name = "Mycroft"

def print_name_box():
  print(name)

  def smaller_box():
    print(name)

    def smallest_box():
      print(name)

    smallest_box()

  smaller_box()

print_name_box()


