import time
import alphasign


def main():
  sign = alphasign.Serial("/dev/ttyUSB0")
  sign.connect()
  sign.clear_memory()

  print("Memory cleared")
  # create logical objects to work with
  counter_str = alphasign.String(size=14, label="1")
  counter_txt = alphasign.Text("%sWelcome to MakersLink            Weeeeeeeee :D      " % alphasign.colors.GREEN, label="A")#, mode=alphasign.modes.HOLD )
  # allocate memory for these objects on the sign
  sign.allocate((counter_str, counter_txt))
  print("Memory allocated")

  # tell sign to only display the counter text
  sign.set_run_sequence((counter_txt,))
  print("Run sequence set")

  # write objects
  for obj in (counter_str, counter_txt):
    sign.write(obj)
    print("Object written")

  # (strictly) monotonically increasing counter
  counter_value = 0
  while True:
    counter_str.data = counter_value
    # sign.write(counter_str)
    # print("Counter written")
    counter_value += 1
    time.sleep(1)


if __name__ == "__main__":
  main()
