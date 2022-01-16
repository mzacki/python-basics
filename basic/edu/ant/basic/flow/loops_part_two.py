# None and len range
# instead of for each
# for i loop using range within length (number of contents) of an array
task_list = ["roof", "elevation - thermal insulation", "chimney", "beer", "furnace", "fence"]
array_length = len(task_list)  # contains 6
# Global variable declaration.
# Without "None" it's impossible.
# Without declaration, we got "not defined" error
task_position = None
print("Today working on {} tasks.".format(str(array_length)))
for index in range(array_length):  # range(6) returns range 0 - 5 -> last index exclusive!
    task_position = index
    if task_list[index] == "beer":
        print("{} found at position {}. I am taking a break!".format(task_list[index].capitalize(), index))
        # both index and task_position may be used here
        break
    print(task_list[index])
print("Let's call it a day! Tasks on positions greater than {} have not been completed. "
      "Not even started.".format(task_position))

# or simply use sth like this
if "beer" in task_list:
    print("Beer drinking stands as task at position {}".format(task_list.index("beer")))

