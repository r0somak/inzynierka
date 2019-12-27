<template>
  <div>
    <b-card-group deck>
      <b-card title="WHO: W 2018r. odra zabiła 142 tys. osób. Większość to dzieci." img-src="https://static.pb.pl/filtered/66/273766,449349.jpg" img-alt="Image" img-top>
        <b-card-text>
          Z raportu Światowej Organizacji Zdrowia (WHO) wynika, że w 2018 roku odrą zaraziło się
          niemal 10 mln
          ludzi na całym świecie, z czego 142 tys. zmarły.
          Większość z ofiar śmiertelnych, to pacjenci
          pediatryczni poniżej piątego roku życia.
        </b-card-text>
        <template v-slot:footer>
          <small class="text-muted">
            <a href="https://pulsmedycyny.pl/who-w-2018-r-odra-zabila-142-tys-osob-wiekszosc-to-dzieci-977478">
              Źródło: Puls Medycyny
            </a>
          </small>
        </template>
      </b-card>

      <b-card title="Dieta ketogeniczna pomaga zwalczyć grypę" img-src="https://static.pb.pl/filtered/51/251729,655615.jpg" img-alt="Image" img-top>
        <b-card-text>
          Dieta ketogeniczna: wysokotłuszczowa i niskowęglowodanowa może ułatwiać
          organizmowi zwalczanie wirusa grypy – informuje pismo „Science Immunology”.
        </b-card-text>
        <template v-slot:footer>
          <small class="text-muted">
            <a href="https://pulsmedycyny.pl/dieta-ketogeniczna-pomaga-zwalczyc-grype-975739">
              Źródło: Puls Medycyny
            </a>
          </small>
        </template>
      </b-card>

      <b-card title="Naukowcy opracowali skuteczniejszą szczepionkę przeciwko wściekliźnie" img-src="https://static.pb.pl/filtered/04/271108,907548.jpg" img-alt="Image" img-top>
        <b-card-text>
          Dodanie określonej cząsteczki immunologicznej do szczepionki przeciwko wściekliźnie może
          znacząco zwiększyć jej skuteczność,
          a co za tym idzie dostępność - ogłosili naukowcy z Thomas Jefferson
          University na łamach „PLOS Neglected Tropical Diseases”.
        </b-card-text>
        <template v-slot:footer>
          <small class="text-muted">
            <a href="https://pulsmedycyny.pl/naukowcy-opracowali-skuteczniejsza-szczepionke-przeciwko-wsciekliznie-975695">
              Źródło: Puls Medycyny
            </a>
          </small>
        </template>
      </b-card>

      <b-card title="Zapadalność na gruźlicę w Polsce przekracza średnią europejską" img-src="https://static.pb.pl/filtered/0e/270350,533084.jpg" img-alt="Image" img-top>
        <b-card-text>
          Czy zasadne jest podawanie noworodkom tuż po porodzie szczepionki przeciwko gruźlicy?
          Nad tym palącym i często powracającym problemem dyskutowali specjaliści podczas VII
          Krajowej Konferencji Naukowo-Szkoleniowej Polskiego Towarzystwa Wakcynologii, która
          odbyła 24-26 października w Poznaniu.
        </b-card-text>
        <template v-slot:footer>
          <small class="text-muted">
            <a href="https://pulsmedycyny.pl/sytuacja-epidemiologiczna-gruzlicy-w-polsce-i-europie-974753">
              Źródło: Puls Medycyny
            </a>
          </small>
        </template>
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
export default {
  name: 'Cards',
};
</script>

<style lang="scss" scoped>
  .card-deck {
    margin: 100px 50px 50px 50px;
  }

</style>
