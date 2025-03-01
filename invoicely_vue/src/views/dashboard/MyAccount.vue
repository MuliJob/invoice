<template>
  <div class="page-my-account">
    <nav class="breadcrumb" aria-label="breadcrumbs">
      <ul>
        <li>
          <router-link to="/dashboard">Dashboard</router-link>
        </li>
        <li class="is-active">
          <router-link to="/dashboard/my-account" aria-current="true">My account</router-link>
        </li>
      </ul>
    </nav>
    <h1 class="title">My Account</h1>

    <strong>Team:</strong>{{ team.name }}<br>
    <strong>Username: </strong>{{ $store.state.user.username }}

    <hr>

    <div class="buttons">
      <router-link to="/dashboard/my-account/edit-team" class="button is-light">Edit team</router-link>
      <button @click="logout()" class="button is-danger">Logout</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast';

export default {
  name: 'MyAccount',
  data() {
    return {
      team: {}
    }
  },
  async mounted() {
    await this.getOrCreateTeam()
  },
  methods: {
    getOrCreateTeam() {
      axios
        .get("http://127.0.0.1:8000/api/v1/teams/")
        .then(response => {
          this.team = response.data[0]
        })
        .catch(error => {
          console.log(JSON.stringify(error))
        })
    },
    logout() {
      axios
        .post("http://127.0.0.1:8000/api/v1/token/logout/")
        .then(response => {
          axios.defaults.headers.common["Authorization"] = ""

          localStorage.removeItem("username")
          localStorage.removeItem("userid")
          localStorage.removeItem("token")

          this.$store.commit('removeToken')

          this.$router.push("/")
          toast({
            message: "You have been logged out",
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: 'bottom-right',
          })
        })
        .catch(error => {
          if (error.response) {
            console.log(JSON.stringify(error.response.data))
          } else if (error.message) {
            console.log(JSON.stringify(error.message))
          } else {
            console.log(JSON.stringify(error))
          }
      })
    }
  }
}
</script>