<template>
    <div class="container">
        <div class="column is-multiline">
            <h1 class="title">
                Clients
            </h1>
        </div>
        <router-link to="/dashboard/clients/add"
         class="button is-success" v-if="$store.state.team.max_clients > num_clients">
         Add Client
        </router-link>

        <div class="notification is-danger"
          v-else>
          You have reached your top limitation, Please Upgrade!
        </div>
        <hr>
        
        <form @submit.prevent="submitForm">
            <div class="field has-addons">
                <div class="control">
                    <input type="text" class="input" v-model="query" placeholder="Search by name">
                </div>
                <div class="control">
                    <button class="button is-success">Search</button>
                </div>

            </div>
        </form>

        <div class="column is-12">
            <template v-if="clients.length">
            <table class="table is-fullwidth">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Contact Person</th>
                    </tr>
                </thead>

                <tbody>
                    <tr v-for="client in clients" v-bind:key="client.id">
                        <td> {{ client.name }}</td>
                        <td> {{ client.contact_person  }}</td>
                        <td> 
                            <router-link :to="{name: 'Client', params: {id: client.id}}">Details</router-link>
                        </td>
                    </tr>
                </tbody>
            </table>
            <div class="buttons">
                <button class="button is-light" @click="goToPreviousPage()" v-if="showPreviousButton">Previous</button>
                <button class="button is-light" @click="goToNextPage()" v-if="showNextButton">Next</button>    
            </div>
         </template>

         <template v-else>
                <p>You don't have any Clietns yet .....</p>
         </template>
        </div>
    </div>
</template>

<script>
import axios from 'axios'


export default {
       name: 'Clients',
       data(){
            return {
                clients: [],
                showNextButton: false,
                showPreviousButton: false,
                currentPage: 1,
                query: '',
                num_clients: 0,
            }
       },
       //when this page is munted use the next function
       mounted() {
         this.getClients()
       },
       methods: {
            goToNextPage(){
                this.currentPage += 1
                this.getClients()
            },
            goToPreviousPage(){
                this.currentPage  -= 1
                this.getClients()
            },
            async getClients(){
                this.$store.commit('setIsLoading', true)

                this.showNextButton = false
                this.showPreviousButton = false

            
            await axios
                .get(`/api/v1/clients/`)
                .then(response => {
                    console.log(response.data)
                    this.num_clients = response.data.count
                 })

                await axios
                        .get(`/api/v1/clients/?page=${this.currentPage}&search=${this.query}`)
                        .then(response => {
                            this.clients = response.data.results

                            console.log(this.clients)

                            if(response.data.next){
                            console.log(response.data)
                            this.showNextButton = true
                            }
                            if(response.data.previous){
                                this.showPreviousButton = true
                            }

                            console.log(response.data.next)
                            
                        })
                        .catch(error => {
                            console.log(error)
                        }) 

                this.$store.commit('setIsLoading', false)
            },
            submitForm(){
                this.getClients()
            }
       }
   }
</script>