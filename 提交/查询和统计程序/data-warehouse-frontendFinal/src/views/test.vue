<template>
  <el-button @click="testpost()">点击发送POST和GET</el-button>
</template>

<script>
export default {
  // eslint-disable-next-line vue/name-property-casing
  name: "test",
  data() {
    return {};
  },
  methods: {
    testpost() {
      // post方法
      this.$axios.post("/post", {
        data: {
          title: "harry",
          date: {
            year: 2022,
            month: 11,
            day: 23
          },
          "director": "",
          actor: "",
          genre: "",
          "score": {
            min: 2,
            max: 4,
          },
          columns: ["title", "asin", "score"],
        }
      }).then(res => {

      }).catch(err => {

      });

      // get方法
      this.$axios.get("/get", {
        params: {
          date: {
            year: 2022,
            month: 4,
          }
        }
      }).then(res => {

      }).catch(err => {

      })
    },
    test() {
      this.$axios.get("/spark/bytime/year", { params: { year: 2008 } });
      this.$axios.get("/mysql/bytime/year", { params: { year: 2008 } });
      this.$axios.get("/neo4j/bytime/year", { params: { year: 2008 } });
    },
  }
}
</script>
