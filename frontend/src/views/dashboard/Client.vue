<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="colunm is-12">
              <h1 class="title">{{ client.name }}</h1>
             <router-link :to="{name: 'EditClient', params: {id: client.id}}" class="button is-light">Edit</router-link>
            </div>
            <div class="column is-12"></div>

            <hr>
          
            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle"><strong>Details</strong></h2>
                    <p><strong>Created At:</strong> {{ client.created_at}}</p>
                    <p><strong>Modified At:</strong> {{ client.modified_at}}</p>

                </div>
            </div>

            <div class="column is-4">
                <div class="box">
                    <h2 class="subtitle"><strong>Contact Information</strong></h2>
                    <p><strong>Contact Person:</strong> {{ client.contact_person}}</p>
                    <p><strong>Email:</strong> {{ client.email}}</p>
                    <p><strong>Phone:</strong> {{ client.phone}}</p>
                    <p><strong>Website:</strong> {{ client.website}}</p>
                </div>
            </div>

            <hr>
            <div class="column is-12">
                <router-link :to="{name: 'AddNote', params: {id: client.id}}" class="button is-success mb-6" >Add Note</router-link>
            </div>

            <div class="column is-12 box"
                 v-for="note in notes"
                 v-bind:key="note.id">
                 <h3 class="is-size-4">{{ note. name }}</h3>
                 <p>
                    {{ note.body }}
                 </p>
                 <router-link :to="{name: 'EditNote', params: {id: client.id, note_id: note.id }}" class="button is-success mt-6" >Edit Note</router-link>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Client',
    data(){
        return {
            client: {},
            notes: []
        }
    },
    mounted(){
        this.getClient()
    },
    methods: {
        async getClient(){
            this.$store.commit('setIsLoading', true)

            const clientID  = this.$route.params.id            
            await axios
                .get(`/api/v1/clients/${clientID}/`)
                .then(response => {
                    this.client = response.data
                })
                .catch(error => {
                    console.log(error);
                });

            await axios
                .get(`/api/v1/notes/?client_id=${clientID}`)
                .then(response => {
                    this.notes = response.data
                })
                .catch(error => {
                    console.log(error);
                });

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>