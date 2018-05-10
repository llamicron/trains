var app = new Vue({
  el: "#main",
  data: {
    volunteers: [],
    roles: [],
    roleMap: {},
    trainings: [],
    selectedRoles: []
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

    getRoleMap() {
      axios.get('/role_map')
        .then(response => {
          console.log(response);
          this.roleMap = response.data;
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
      updates = ['trainings', 'roles', 'volunteers', 'roleMap']

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
    },

    selectRole(code) {
      i = this.selectedRoles.indexOf(code);
      if (i == -1) {
        this.selectedRoles.push(code)
      } else {
        this.selectedRoles.splice(i, 1)
      }
    },

    everyRoleSelected() {
      codes = this.roles.map(x => x.code)
      this.selectedRoles.forEach(code => {
        if (codes.indexOf(code) == -1) {
          return false;
        }
      });
      return true;
    },

    toggleAllRoles() {
      if (this.everyRoleSelected()) {
        this.selectedRoles = []
      } else [
        this.selectedRoles = this.roles.map(x => x.code)
      ]
    }
  },

  mounted() {
    this.updateAll();
  },

  computed: {
    aThird: function () {
      return Math.ceil(this.roles.length / 3)
    }
  }
})
