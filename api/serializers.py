from rest_framework import serializers
from rest_framework.authtoken.models import Token
from database.models import CustomUser, Pacjent


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'password',
        )
        extra_kwargs = {
            'password':
                {
                    'write_only': True
                }
        }

    def create(self, validated_data):
        pacjent = Pacjent()
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username'],
            fk_id_pacjent=pacjent.id,
        )
        user.set_password(validated_data['password'])
        pacjent.save()
        user.save()
        Token.objects.create(user=user)
        return user
