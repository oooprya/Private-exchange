<script setup>
defineProps({
  msg: {
    type: String,
    required: true,
  },
})
</script>

<template>
    <section class="exchange_currency_form">
      <div class="container">
        <div class="flex-row">
          <div class="text-left">
            <h1>{{ msg }}</h1>
            <p>Введите сумму которую хотите продать или купить и нажмите кнопку для поиска обменных пунктах рядом с вами</p>
          </div>
          <div class="main_form">
          </div>
        </div>
    </div>
  </section>
</template>

<style scoped>

</style>
