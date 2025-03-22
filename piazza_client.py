from piazza_api import Piazza

p = Piazza()

email = ""
password = ""
p.user_login(email, password)
print("Successfully logged in!")

courses = p.get_user_classes()
for course in courses:
    print(course)

class_id = "m6pcnpehsnh68g"
network = p.network(class_id)
feed = network.get_feed(limit=10)

meta = network.get_feed(limit=10)  # Meta contains instructor list
instructor_uids = {instr['uid'] for instr in meta['instructors']}

print("\nLatest Posts in 540:")
for post in feed["feed"]:
    post_id = post["nr"]
    post_data = network.get_post(post_id)
    
    print(f"\nPost #{post_id}")
    print(f"Subject: {post_data['history'][0]['subject']}")
    print(f"Content: {post_data['history'][0]['content']}\n")
    print("-" * 50)
    print(f"Comments for Post #{post_id}:")

    print("Instructor Answers:")
    found_instructor_answer = False
    # Loop over the subsequent entries in the history (the replies)
    for comment in post_data["history"][1:]:
        if comment.get('uid') in instructor_uids:
            print(f"- {comment['content']}")
            found_instructor_answer = True
    if not found_instructor_answer:
        print("No instructor answer yet.")
