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

          this.volunteers = response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    getRoles() {
      axios.get('/roles')
        .then(response => {
          this.roles = response.data;
          return response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    getRoleMap() {
      axios.get('/role_map')
        .then(response => {

          this.roleMap = response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    getTrainings() {
      axios.get('/trainings')
        .then(response => {

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
            this[element] = response.data;
          })
          .catch(function (error) {
            console.log(error);
          });
      });
    },

    toggleRoleSelect(roleCode) {
      roleCode = String(roleCode);
      index = this.selectedRoles.indexOf(roleCode);
      if (index == -1) {
        this.selectedRoles.push(roleCode);
      } else {
        this.selectedRoles.splice(index, 1)
      }
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
