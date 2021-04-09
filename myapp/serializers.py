from rest_framework import serializers

from myapp.models import Lewenilotu, Matasiga, Veitokani, Valenilotu, Veitosoyaki, Veivakalotutaki, Bulararaba

class LewenilotuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lewenilotu
        fields = ('id',
                'yaca_ni_vuvale',
                'lewenilotu',
                'tiki_ni_siganisucu',
                'tagane_se_yalewa',
                'phone_contact',
                'email_contact',
                'Adress',
                'tutu_vakalotu',
                'tavi_vakalotu',
                'matasiga',
                'veitokani',
                'valenilotu',
                'vuli_keina_cakacaka')

class MatasigaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matasiga
        fields = ('id',
                'matasiga',
                'liuliu_ni_matasiga',
                'valenilotu',
                'vanua_dau_soqoni_kina',
                'veika_dau_qaravi',
                'vakamacala_tale_eso')

class VeitokaniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veitokani
        fields = ('id',
                'veitokani',
                'liuliu_ni_veitokani',
                'vunivola_ni_veitokani',
                'dauniyau_ni_veitokani',
                'valenilotu',
                'levu_ni_lavo_bula',
                'veika_dau_qaravi',
                'vakamacala_tale_eso')

class ValenilotuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valenilotu
        fields = ('id',
                'valenilotu',
                'yaca_ni_vakatawa',
                'vukevuke_ni_vakatawa',
                'tuirara',
                'vukevuke_ni_tuirara',
                'vunivola',
                'dauniyau',
                'address',
                'phone_contact',
                'vakamacala_tale_eso')

class VeitosoyakiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veitosoyaki
        fields = ('id',
                'yacana',
                'lewenilotu',
                'toki',
                'siga_e_yaco_kina',
                'vola',
                'vakamacala_tale_eso')

class VeivakalotutakiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veivakalotutaki
        fields = ('id',
                'yacani_programi',
                'gauna_vakayacori_kina',
                'vakamacala_tale_eso')
                 
class BulararabaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bulararaba
        fields = ('id',
                'veika_e_vakayacori',
                'gauna_vakayacori_kina',
                'vakamacala_tale_eso')