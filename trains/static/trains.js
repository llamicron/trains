var app = new Vue({
  el: "#main",
  data: {
    roles: [],
    emailText: 'Hi {name},\n\nYou have a few incomplete trainings. They are:\n\n{trainings}\n\nThanks!',
    emailPreviewText: '',
    selectedRoles: [],
    allRoles: false,
    sendText: 'Send',
    exampleVolunteer: {
      name: "John Doe",
      unit: "Troop 999",
      trainings: ['Safety Afloat', 'Youth Protection Training'],
    }
  },

  methods: {
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
    },

    processEmailExampleText() {
      this.emailPreviewText = this.emailText;
      this.emailPreviewText = this.emailPreviewText.replace('{name}', this.exampleVolunteer.name);
      this.emailPreviewText = this.emailPreviewText.replace('{trainings}', this.exampleVolunteer.trainings.join(', '));
    },

    send() {
      if (this.sendText == 'Send') {
        this.sendText = "Are you sure?";
      } else {
        if (this.emailText == '' || this.selectedRoles.length == 0) {
          this.showSnackbar('Please fill everything in');
          return false;
        }
        console.log(this.selectedRoles);
        axios.post('/send', {
          email_text: this.emailText,
          sent_roles: this.selectedRoles
        }).then(response => {
          console.log(response);
        }).catch(error => {
          console.log(error);
        })

        this.showSnackbar('Email sent');
        this.sendText = 'Send';
      }
    },

    showSnackbar(message) {
      snackbarContainer = document.querySelector('#sent-snackbar');
      var data = {
        message: message,
        timeout: 2000,
      };
      snackbarContainer.MaterialSnackbar.showSnackbar(data);
    }
  },

  mounted() {
    this.getRoles();
    this.processEmailExampleText();
  },

  computed: {
    aThird: function () {
      return Math.ceil(this.roles.length / 3)
    }
  },

  watch: {
    allRoles: function() {
      this.allRolesOn(this.allRoles);
    },
    emailText: function() {
      this.processEmailExampleText();
    }
  },
})

