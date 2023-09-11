from PersonFile import Person
from InterceptorFile import Interceptor
p1 = Person()
p2 = Person()
p1.request_name()
p2.request_name()
villain = Interceptor()

clock, base = p1.pick_clock_and_base()
print(f"{p1.name} has sent clock = {clock} and base={base}.")
villain.intercept_clock_and_base(clock=clock, base=base)
print(f"Sending clock = {clock} and base = {base} to {p2.name}.")
p2.receive_clock_and_base(clock, base)

ppn1 = p1.select_private_key_and_generate_ppn()
print(f"{p1.name} has just sent public-private key {ppn1}.")
villain.intercept_ppn(ppn1)
print(f"Sending public-private key {ppn1} to {p2.name}.")
p2.receive_friend_ppn(ppn1)

ppn2 = p2.select_private_key_and_generate_ppn()
print(f"{p2.name} has just sent public-private key {ppn2}.")
villain.intercept_ppn(ppn2)
print(f"Sending public-private key {ppn2} to {p1.name}.")
p1.receive_friend_ppn(ppn2)

p1.calculate_shared_secret()
p2.calculate_shared_secret()

scrambled1 = p1.encode_message()
print(f"{p1.name} has just sent message: \"{scrambled1}\" to {p2.name}.")
decoded_string1 = p2.decode_message(scrambled1)
print(f"{p2.name} just decoded message: \"{decoded_string1}\"")

scrambled2 = p2.encode_message()
print(f"{p2.name} has just replied with message: \"{scrambled2}\" to {p1.name}.")
decoded_string2 = p1.decode_message(scrambled2)
print(f"{p1.name} just decoded response: \"{decoded_string2}\"")

print("--------------------------------------------------")
print("**** Interceptor is now trying to decode messages.")
villain.hack_message(scrambled1)
villain.hack_message(scrambled2)
