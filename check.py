from streamlit_app import run

def testModel():
    source = "The Balkan terrapin or western Caspian terrapin (Mauremys rivulata) is a species of terrapin in the family Geoemydidae. It is found in the eastern Mediterranean region. While technically omnivorous, the terrapins are known to prefer meat. They can grow to 25 cm in carapace length, although hatchlings are usually only 3 to 4 cm in length.It is found in the Balkan Peninsula (Albania, Bosnia and Herzegovina, Bulgaria, Croatia, North Macedonia, Montenegro, Serbia, Greece), a number of Mediterranean islands including Crete, Lesvos and Cyprus, and in the Middle East (Israel, Jordan, Lebanon, Syria, Turkey).[4] On some Greek and Turkish islands where the terrapins are found, they may be threatened with extirpation"
    query_text = "What is Balkan"
    inputs = [
        {
            "role": "system",
            "content": "You are an expert, who responds to user's questions according to the source document they provide. The Source document will be in between symbol of #####. And the user query will be inside XXXXX",
        },
        {
            "role": "user",
            "content": f"Answer the following question according to ##### \n {source} \n##### \n\n\n\n\n , Question is XXXXX \n{query_text}\n XXXXX",
        },
    ]
    res = run("@cf/meta/llama-2-7b-chat-int8", inputs)
    data = res["result"]["response"]
    failed = False

    if type(data) != str :
        print("🔴 Response is not a string")
        failed = True

    if len(data) == 0:
        print("🔴 Response size is 0")
        failed = True

    if failed:
        print("Failed")
        return

    print("✅All test cases passed")


testModel()
