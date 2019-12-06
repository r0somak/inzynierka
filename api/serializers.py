from rest_framework import serializers
from rest_framework.authtoken.models import Token
from database.models import CustomUser, Pacjent, Lekarz, Przychodnia


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
            'id',
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
        extra_kwargs = {
            'id':
                {
                    'read_only': True
                }
        }


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
            'id',
            'name',
            'surname',
            'specjalizacja',
            'nr_pwz',
            'telefon',
        )
        extra_kwargs = {
            'id':
                {
                    'read_only': True
                }
        }


class PrzychodniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Przychodnia
        fields = (
            'id',
            'nazwa',
            'ulica',
            'nr_ulicy',
            'nr_mieszkania',
            'kod_pocztowy',
            'miasto',
            'wojewodztwo',
            'email',
            'telefon',
            'lekarze',
        )
        extra_kwargs = {
            'id':
                {
                    'read_only': True
                }
        }
