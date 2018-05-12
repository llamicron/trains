var app = new Vue({
  el: "#main",
  data: {
    volunteers: [],
    roles: [],
    roleMap: {},
    trainings: [],
    selectedRoles: [],
    allRoles: false
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

    // Switches a single role code
    toggleRoleSelect(roleCode) {
      roleCode = String(roleCode);
      index = this.selectedRoles.indexOf(roleCode);
      if (index == -1) {
        this.selectedRoles.push(roleCode);
      } else {
        this.selectedRoles.splice(index, 1)
      }
    },

    // Turns all the roles on or off with the 'everyone' switch
    allRolesOn(on=true) {
      if (on) {
        this.allRoleSwitchesOn();
        this.selectedRoles = this.roles.map(x => String(x.code));
      } else {
        this.allRoleSwitchesOn(false);
        this.selectedRoles = [];
      }
    },

    // The MDL switches won't toggle on there own. Need to do it manually. This is only the appearance of the switch.
    allRoleSwitchesOn(on=true) {
      switches = document.getElementsByClassName('roleSwitch');

      for (let i = 0; i < switches.length; i++) {
        const sw = switches[i].parentElement.MaterialCheckbox;
        if (on) {
          sw.check();
        } else {
          sw.uncheck();
        }
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
  },

  watch: {
    allRoles: function() {
      this.allRolesOn(this.allRoles);
    }
  },
})
