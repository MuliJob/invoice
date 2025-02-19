<template>
  <div class="page-add-invoice">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Add Invoices</h1>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast';

export default {
  name: "AddInvoice",
  data() {
    return {
      invoice: {}
    }
  }
}
</script>