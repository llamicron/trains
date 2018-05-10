var app = new Vue({
  el: "#main",
  data: {
    volunteers: [],
    roles: {},
    trainings: [],
  },

  methods: {
    getVolunteers() {
      axios.get('/volunteers')
        .then(response => {
          console.log(response);
          this.volunteers = response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    getRoles() {
      axios.get('/roles')
        .then(response => {
          console.log(response);
          this.roles = response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    getTrainings() {
      axios.get('/trainings')
        .then(response => {
          console.log(response);
          this.trainings = response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    updateAll() {
      // Updates the following
      updates = ['trainings', 'roles', 'volunteers']

      updates.forEach(element => {
        axios.get('/' + element)
          .then(response => {
            console.log(response);
            this[element] = response.data;
          })
          .catch(function (error) {
            console.log(error);
          });
      });
    }
  },

  mounted() {
    this.updateAll();
  }
})
