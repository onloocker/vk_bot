from src.vkbot import VkBot

token = "5277d48df2317b0597d43fa36fb0b694bc50f6496a516cb4f62ec4e26098a4efd157a155b01230cc46635"  # Bot's token.
targets = ["id1", "pagislav"]  # Example: "id1" or "1" or 1 - Pavel Durov's page, "pagislav" - my page.
album = "saved"  # put saved , wall or profile .

try:
    VkBot.likes_from_bot(target_ids=targets, album=album, token=token)
except Exception as e:
    print(e)