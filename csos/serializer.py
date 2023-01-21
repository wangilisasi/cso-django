from rest_framework import serializers
#IMAGE_SIZE_MAX_BYTES = 1024 * 1024 * 2 # 2MB
MIN_TITLE_LENGTH = 5
MIN_BODY_LENGTH = 50

from .models import Cso
class CsoSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username_from_author')
    class Meta:
        model=Cso
        fields=['pk','name','description','author','username','date_published']

    def get_username_from_author(self,cso):
        username = cso.author.username
        return username

#Serializer for updating the three fields of Cso
class CsoUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cso
		fields = ['name', 'description']

	#Override the validate method to validate some fileds b4 saving to database
	def validate(self, cso):
		try:
			name = cso['name']
			if len(name) < MIN_TITLE_LENGTH:
				raise serializers.ValidationError({"response": "Enter a title longer than " + str(MIN_TITLE_LENGTH) + " characters."})
			
			description = cso['description']
			if len(description) < MIN_BODY_LENGTH:
				raise serializers.ValidationError({"response": "Enter a body longer than " + str(MIN_BODY_LENGTH) + " characters."})
			
			# image = blog_post['image']
			# url = os.path.join(settings.TEMP , str(image))
			# storage = FileSystemStorage(location=url)

			# with storage.open('', 'wb+') as destination:
			# 	for chunk in image.chunks():
			# 		destination.write(chunk)
			# 	destination.close()

			# Check image size
			# if not is_image_size_valid(url, IMAGE_SIZE_MAX_BYTES):
			# 	os.remove(url)
			# 	raise serializers.ValidationError({"response": "That image is too large. Images must be less than 2 MB. Try a different image."})

			# # Check image aspect ratio
			# if not is_image_aspect_ratio_valid(url):
			# 	os.remove(url)
			# 	raise serializers.ValidationError({"response": "Image height must not exceed image width. Try a different image."})

			# os.remove(url)
		except KeyError:
			pass
		return cso

class CsoCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cso
		fields = ['name', 'description', 'date_updated', 'author']

	def save(self):	
		try:
			#image = self.validated_data['image']
			name = self.validated_data['name']
			if len(name) < MIN_TITLE_LENGTH:
				raise serializers.ValidationError({"response": "Enter a title longer than " + str(MIN_TITLE_LENGTH) + " characters."})
			
			description = self.validated_data['description']
			if len(description) < MIN_BODY_LENGTH:
				raise serializers.ValidationError({"response": "Enter a body longer than " + str(MIN_BODY_LENGTH) + " characters."})
			
			cso = Cso(
								author=self.validated_data['author'],
								name=name,
								description=description,
								)

			# url = os.path.join(settings.TEMP , str(image))
			# storage = FileSystemStorage(location=url)

			# with storage.open('', 'wb+') as destination:
			# 	for chunk in image.chunks():
			# 		destination.write(chunk)
			# 	destination.close()

			# # Check image size
			# if not is_image_size_valid(url, IMAGE_SIZE_MAX_BYTES):
			# 	os.remove(url)
			# 	raise serializers.ValidationError({"response": "That image is too large. Images must be less than 2 MB. Try a different image."})

			# # Check image aspect ratio
			# if not is_image_aspect_ratio_valid(url):
			# 	os.remove(url)
			# 	raise serializers.ValidationError({"response": "Image height must not exceed image width. Try a different image."})

			# os.remove(url)
			cso.save()
			return cso
		except KeyError:
			raise serializers.ValidationError({"response": "You must have a title and some content"})