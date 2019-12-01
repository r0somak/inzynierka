from rest_framework import serializers
from rest_framework.authtoken.models import Token
from database.models import CustomUser, Pacjent, Lekarz


class UserSerializer(serializers.ModelSerializer):
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
        pacjent.save()
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username'],
            fk_id_pacjent=pacjent,
        )
        user.set_password(validated_data['password'])

        user.save()
        Token.objects.create(user=user)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacjent
        fields = (
            'name',
            'surname',
            'pesel',
            'ulica',
            'nr_ulicy',
            'nr_mieszkania',
            'kod_pocztowy',
            'miasto',
            'wojewodztwo',
            'telefon',
            'dokumenty',
        )


class DoctorSerializer(serializers.ModelSerializer):
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
        lekarz = Lekarz()
        lekarz.save()
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username'],
            fk_id_lekarz=lekarz,
        )
        user.set_password(validated_data['password'])

        user.save()
        Token.objects.create(user=user)
        return user


class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lekarz
        fields = (
            'name',
            'surname',
            'specjalizacja',
            'nr_pwz',
            'telefon',
        )
