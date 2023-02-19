from pavilion_cms import PavilionCMS

client = PavilionCMS(read_token="04d9f9e9db9241ac86b29cbe9289bb6a")

response = client.tags.all()
import pdb; pdb.set_trace()

# all_tags = pavilioncms.get_all_tags()

# assert all_tags

# print(all_tags)

# single_id = all_tags["results"][0]["id"]

# single_tag = pavilioncms.get_tag(tag_id=single_id)
# print(single_tag)