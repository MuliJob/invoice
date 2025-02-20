<template>
  <div class="page-add-invoice">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Add Invoices</h1>
      </div>

      <div class="column is-12">
        <h2 class="is-size-5 mb-4">Client</h2>

        <div class="select">
          <select name="client" v-model="invoice.client">
            <option value="" selected>---Select client---</option>
            <option
              v-for="client in clients"
              v-bind:key="client.id"
              v-bind:value="client"
            >
              {{ client.name }}
            </option>
          </select>
        </div>

        <div class="box mt-4" v-if="invoice.client">
          <p><strong>{{ invoice.client.name }}</strong></p>
          <p><strong>Email:</strong> {{ invoice.client.name }}</p>
          <p v-if="invoice.client.address1">{{ invoice.client.address1 }}</p>
          <p v-if="invoice.client.address2">{{ invoice.client.address2 }}</p>
          <p v-if="invoice.client.zipcode|| invoice.client.place">{{ invoice.client.zipcode }} {{ invoice.client.place }}</p>
          <p v-if="invoice.client.country">{{ invoice.client.country }}</p>
        </div>
      </div>

      <div class="column is-12">
        <h2 class="is-size-5 mb-4">Items</h2>

        <ItemForm
          v-for="item in invoice.items"
          v-bind:key="item.item_num"
          v-bind:initialItem="item"
        ></ItemForm>

        <button class="button is-light" @click="addItem">
          +
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast';
import ItemForm from '@/components/ItemForm.vue';

export default {
  name: "AddInvoice",
  components: {
    ItemForm
  },
  data() {
    return {
      invoice: {
        client: '',
        items: [
          {
            item_num: 0,
            title: '',
            unit_price: '',
            quantity: 1,
            vat_rate: 0,
            net_amount: 0
          }
        ]
      },
      clients: []
    }
  },
  async mounted() {
    await this.getClients()
  },
  methods: {
    getClients() {
      axios
        .get("http://127.0.0.1:8000/api/v1/clients/")
        .then(response => {
          this.clients = response.data
        })
        .catch(error => {
          console.log(JSON.stringify(error))
        })
    },
    addItem() {
      this.invoice.items.push(
        {
            item_num: this.invoice.items.length,
            title: '',
            unit_price: '',
            quantity: 1,
            vat_rate: 0,
            net_amount: 0
          }
      )
    }
  }
}
</script>

<style lang="scss">
  .select, .select select {
    width: 100%;
  }
</style>