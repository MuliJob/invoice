<template>
  <div class="page-signup">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Sign Up</h1>

        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Email</label>
            <div class="control">
              <input type="email" name="username" class="input" v-model="username">
            </div>
          </div>

          <div class="field">
            <label>Password</label>
            <div class="control">
              <input type="password" name="password" class="input" v-model="password">
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p
              v-for="error in errors"
              v-bind:key="error"  
            >
              {{ error }}
            </p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-success">Sign up</button>
            </div>
          </div>
        </form>
        <hr>
        <router-link to="/log-in">Click here</router-link> to log in!
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast';

export default {
  name: 'SignUp',
  data () {
    return {
      username: '',
      password: '',
      errors: []
    }
  },
  methods: {
    submitForm(e) {
      const formData = {
       username: this.username,
       password: this.password
      }

      axios
        .post("http://127.0.0.1:8000/api/v1/users/", formData)
        .then(response => {
          console.log(response)

          this.$router.push('/log-in')
          toast({
            message: "User created successful",
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: 'bottom-right',
          })
        })
        .catch(error => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`)
            }
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