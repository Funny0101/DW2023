<!-- eslint-disable no-unused-vars -->
<!-- eslint-disable vue/singleline-html-element-content-newline -->
<!-- eslint-disable vue/max-attributes-per-line -->
<!-- eslint-disable vue/require-v-for-key -->
<template>
  <div class="app-container">
    <!-- <el-dialog
      title="电影详情"
      :visible.sync="dialogVisible"
      width="25%"
      center
      @close="dialogVisible = false"
    >
      <div>
        <p>asin:{{ dialogData.asin }}</p>
        <p>电影名:{{ dialogData.name }}</p>
        <p v-if="dialogData.director.length !== 0">
          导演：
          <span v-for="i in dialogData.director">{{ i }}, </span>
        </p>
        <p v-if="dialogData.actor.length !== 0">
          演员：
          <span v-for="i in dialogData.actor">{{ i }}, </span>
        </p>
        <p>评分:{{ dialogData.score }}</p>
        <p>评论总数:{{ dialogData.commentNum }}</p>
      </div>
      <div slot="footer">
        <el-button type="primary" @click="viewOriginWeb()"
          >查看原始网页</el-button
        >
        <br /><br />
        <el-button @click="dialogVisible = false">关闭</el-button>
      </div>
    </el-dialog> -->
    <el-row style="height: 50vh">
      <el-col :span="12">
        <el-form ref="form" :model="form" label-width="120px" style="padding-top: 5vh">
          <el-form-item label="关系来源">
            <el-select v-model="form.source" class="m-2" placeholder="Select" size="small"
              style="width: 75px; margin-right: 15px">
              <el-option label="演员" value="actor"></el-option>
              <el-option label="导演" value="director"></el-option>
            </el-select>
          </el-form-item>
          <!-- <el-autocomplete
              v-if="form.source == 'actor'"
              v-model="form.name"
              :fetch-suggestions="actorSearchSuggest"
              placeholder="请输入演员名"
              style="width: 15vw"
              clearable
              @select="handleSelect"
              size="small"
            />
            <el-autocomplete
              v-if="form.source == 'director'"
              v-model="form.name"
              :fetch-suggestions="directorSearchSuggest"
              placeholder="请输入导演名"
              style="width: 15vw"
              clearable
              @select="handleSelect"
              size="small"
            /> -->

          <el-form-item label="合作对象" style="margin-top: 5vh">
            <el-input v-model="form.target" class="m-2" size="small" style="width: 75px; margin-right: 15px"
              :readonly="true" />
          </el-form-item>

          <!-- <el-form-item label="合作次数" style="margin-top: 5vh">
            <span style="margin-left: 10px; margin-right: 15px">大于</span>
            <el-input
              v-model="form.times"
              size="small"
              :min="0"
              controls-position="right"
              style="width: 50px"
              :readonly="true"
            />
            <span style="margin-left: 15px">次</span>
          </el-form-item> -->
        </el-form>
        <div style="text-align: center">
          <el-button type="primary" @click="search(form)" size="small" style="margin-left: 3vh; margin-top: 10px"
            plain>查询</el-button>
          <el-form ref="form" :model="form" label-width="120px" style="padding-top: 5vh">
            <el-form-item label="最受关注(评论最多)的演员组合" label-width="250px">
            </el-form-item>
            <el-form-item label="电影类型">
              <el-autocomplete v-model="form.genre" :fetch-suggestions="genreSearchSuggest" placeholder="请输入电影类型"
                style="width: 20vw" clearable @select="handleSelect" size="small" />
            </el-form-item>
          </el-form>
          <el-button type="primary" @click="searchPopular(form.genre)" size="small"
            style="margin-left: 3vh; margin-top: 10px" plain>查询</el-button>
        </div>
      </el-col>
      <el-col :span="1">
        <el-divider direction="vertical" />
      </el-col>
      <el-col :span="10">
        <el-tabs v-model="activeName" @tab-click="handleClick">
          <el-tab-pane label="查询结果" name="search">
            <el-table :data="result" v-loading="isLoading" element-loading-text="正在为您查询..." stripe style="width: 100%"
              height="400">
              <el-table-column prop="name1" label="合作者1" width="100" />
              <el-table-column prop="name2" label="合作者2" width="100" />
              <el-table-column prop="times" label="合作次数" width="100" />
              <!--<el-table-column prop="title" label="合作电影" width="250">
                <template slot-scope="scope">
                  <div v-for="(item, index) in scope.row.title" :key="index">
                    {{ item }}
                  </div>
                </template>
              </el-table-column>-->
              <!-- <div slot="empty" style="text-align: left;">
                <el-empty :image-size="100" description="裂开"></el-empty>
              </div> -->
            </el-table>
            <el-row style="text-align: center; margin-top: 20px">
              <el-pagination layout="prev, pager, next, jumper" :current-page.sync="currentPage" :page-size="5"
                :page-count="totalPage" @current-change="getNewPage(form)" small />
            </el-row>
          </el-tab-pane>
          <el-tab-pane label="耗时对比" name="speed">
            <div id="speed" style="width: 400px; height: 400px"></div>
          </el-tab-pane>
        </el-tabs>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "RelationSearch",
  data() {
    return {
      activeName: "search",
      isLoading: false,
      dialogVisible: false,
      result: [],
      mysql_speed: 0,
      spark_speed: 0,
      neo4j_speed: 0,
      dialogData: {
        asin: "1234",
        name: "11",
        director: ["小明", "小红", "小黑", "小白"],
        actor: ["小蓝", "小黄", "小黑", "小白"],
        score: 2.5,
        commentNum: 100,
      },
      form: {
        source: "actor",
        target: "演员",
        name: "",
        times: 5,
      },
      currentPage: 1,
      totalPage: 0,
    };
  },

  mounted() {
    this.echartsInit();
  },

  watch: {
    //监听速度变化，重新渲染页面
    mysql_speed: {
      handler(newValue, oldValue) {
        this.mysql_speed = newValue;
        this.echartsInit();
      },
    },
    spark_speed: {
      handler(newValue, oldValue) {
        this.spark_speed = newValue;
        this.echartsInit();
      },
    },
    neo4j_speed: {
      handler(newValue, oldValue) {
        this.neo4j_speed = newValue;
        this.echartsInit();
      },
    },
  },

  methods: {
    handleSelect(item) {
      console.log(item);
    },

    handleClick(tab, event) {
      console.log(tab, event);
    },

    // directorSearchSuggest(queryString, cb) {
    //   //导演搜索建议
    //   this.$axios
    //     .get("/mysql/suggest/director", {
    //       params: {
    //         director: queryString,
    //         amount: 10,
    //       },
    //     })
    //     .then((res) => {
    //       console.log(res);
    //       var result = [];
    //       for (var i = 0; i < res.suggestions.length; i++) {
    //         result.push({ value: res.suggestions[i] });
    //       }
    //       console.log("这是result", result);
    //       cb(result);
    //     })
    //     .catch((err) => {
    //       this.$message.error("当前网络异常，请稍后再试");
    //     });
    // },

    // actorSearchSuggest(queryString, cb) {
    //   //演员搜索建议
    //   this.$axios
    //     .get("/mysql/suggest/actor", {
    //       params: {
    //         actor: queryString,
    //         amount: 10,
    //       },
    //     })
    //     .then((res) => {
    //       console.log(res);
    //       var result = [];
    //       for (var i = 0; i < res.suggestions.length; i++) {
    //         result.push({ value: res.suggestions[i] });
    //       }
    //       console.log("这是result", result);
    //       cb(result);
    //     })
    //     .catch((err) => {
    //       this.$message.error("当前网络异常，请稍后再试");
    //     });
    // },

    search(form) {
      //判断是否有值为空
      // if (form.name == "") {
      //   this.$message.warning("请输入姓名!");
      // } else
      if (form.source == "director" && form.target == "director") {
        this.$message.warning("关系来源和合作对象不能同时为导演!");
      } else {
        this.isLoading = true;
        //mysql查询总数
        this.$axios
          .post("/relation/count", {
            source: form.source,
            //target: form.target,
            //name: form.name,
            //times: form.times,
            page: 1,
            per_page: 5,
          })
          .then((res) => {
            console.log("pages", res.pages);
            this.totalPage = res.pages;
          })
          .catch((err) => {
            this.$message.error("当前mysql网络异常，请稍后再试");
          });

        //mysql关系查询
        this.$axios
          .post("/relation/detail", {
            source: form.source,
            // target: form.target,
            // name: form.name,
            // times: form.times,
            page: 1,
            per_page: 5,
          })
          .then((res) => {
            console.log(res);
            this.result = res.data;
            console.log("mysql结果", this.result);
            this.mysql_speed = res.consuming_time;
            this.isLoading = false;
          })
          .catch((err) => {
            this.$message.error("当前mysql网络异常，请稍后再试");
          });
        //hive关系查询
        this.$axios
          .post("/hive/relation/detail", {
            source: form.source,
            // target: form.target,
            // name: form.name,
            // times: form.times,
            page: 1,
            per_page: 5,
          })
          .then((res) => {
            console.log(res);
            this.spark_speed = res.consuming_time;
          })
          .catch((err) => {
            this.$message.error("当前spark网络异常，请稍后再试");
          });

        if (form.source == "actor") {
          //neo4j关系查询
          this.$axios
            .get("/neo4j/actors/frequent-actors", {
              params: {
                page: 1,
                per_page: 5,
              }

            })
            .then((res) => {
              console.log(res);
              this.neo4j_speed = res.time;
            })
            .catch((err) => {
              this.$message.error("当前neo4j网络异常，请稍后再试");
            });
        }
        else if (form.source == "director") {
          this.$axios
            .get("/neo4j/actors/frequent-directors", {
              params: {
                page: 1,
                per_page: 5,
              }

            })
            .then((res) => {
              console.log(res);
              this.neo4j_speed = res.time;
            })
            .catch((err) => {
              console.log(err);
              this.$message.error("当前neo4j网络异常，请稍后再试");
            });
        }

        //neo4j关系查询
        // this.$axios
        //   .post("/neo4j/comprehensive/relation", {
        //     source: form.source,
        //     target: form.target,
        //     name: form.name,
        //     times: form.times,
        //     page: 1,
        //     per_page: 5,
        //   })
        //   .then((res) => {
        //     console.log(res);
        //     this.neo4j_speed = res.consuming_time;
        //   })
        //   .catch((err) => {
        //     this.$message.error("当前neo4j网络异常，请稍后再试");
        //   });


      }
    },

    searchPopular(genre) {
      //判断是否有值为空
      // if (form.name == "") {
      //   this.$message.warning("请输入姓名!");
      // } els
      this.isLoading = true;
      //mysql查询总数
      // this.$axios
      //   .get("/relation/popular/count", {
      //     // source: form.source,
      //     //target: form.target,
      //     //name: form.name,
      //     //times: form.times,
      //     params:{
      //     genre:genre,
      //     page: 1,
      //     per_page: 5,
      //     }
      //   })
      //   .then((res) => {
      //     console.log("pages", res.pages);
      //     this.totalPage = res.pages;
      //   })
      //   .catch((err) => {
      //     this.$message.error("当前mysql网络异常，请稍后再试");
      //   });

      //mysql关系查询
      this.$axios
        .get("/relation/popular", {
          // source: form.source,
          // target: form.target,
          // name: form.name,
          // times: form.times,
          params: {
            genre: genre,
            // page: 1,
            // per_page: 5,
          }
        })
        .then((res) => {
          console.log(res);
          this.result = res.data;
          console.log("mysql结果", this.result);
          this.mysql_speed = res.consuming_time;
          this.isLoading = false;
        })
        .catch((err) => {
          this.$message.error("当前mysql网络异常，请稍后再试");
        });

      //neo4j关系查询
      this.$axios
        .get("/neo4j/actors/most-attracted-group-2", {
          params: {
            genre: genre
          }
          // source: form.source,
          // target: form.target,
          // name: form.name,
          // times: form.times,
          // page: 1,
          // per_page: 5,
        })
        .then((res) => {
          console.log(res);
          this.neo4j_speed = res.time;
        })
        .catch((err) => {
          this.$message.error("当前neo4j网络异常，请稍后再试");
        });

      //hive关系查询
      this.$axios
        .get("/hive/relation/popular", {
          params: {
            genre: genre,
          }
        })
        .then((res) => {
          console.log(res);
          this.spark_speed = res.consuming_time;
        })
        .catch((err) => {
          this.$message.error("当前spark网络异常，请稍后再试");
        });
    },

    genreSearchSuggest(queryString, cb) {
      //类型搜索建议
      this.$axios
        .get("/recommend/genre", {
          params: {
            genre: queryString || "",
            amount: 10,
          },
        })
        .then((res) => {
          console.log(res);
          var result = [];
          for (var i = 0; i < res.suggestions.length; i++) {
            result.push({ value: res.suggestions[i] });
          }
          console.log("这是result", result);
          cb(result);
        })
        .catch((err) => {
          this.$message.error("当前网络异常，请稍后再试");
        });
    },

    getNewPage(form) {
      this.isLoading = true;
      //mysql关系查询
      this.$axios
        .post("/relation/detail", {
          source: form.source,
          target: form.target,
          name: form.name,
          times: form.times,
          page: this.currentPage,
          per_page: 5,
        })
        .then((res) => {
          console.log(res);
          this.result = res.data;
          console.log(this.result);
          this.isLoading = false;
          this.mysql_speed = res.consuming_time;
        })
        .catch((err) => {
          this.$message.error("当前mysql网络异常，请稍后再试");
        });
      //hive关系查询
      this.$axios
        .post("/hive/relation/detail", {
          source: form.source,
          // target: form.target,
          // name: form.name,
          // times: form.times,
          page: this.currentPage,
          per_page: 5,
        })
        .then((res) => {
          console.log(res);
          this.spark_speed = res.consuming_time;
        })
        .catch((err) => {
          this.$message.error("当前spark网络异常，请稍后再试");
        });

      if (form.source == "actor") {
        //neo4j关系查询
        this.$axios
          .get("/neo4j/actors/frequent-actors", {
            params: {
              page: this.currentPage,
              per_page: 5,
            }

          })
          .then((res) => {
            console.log(res);
            this.neo4j_speed = res.time;
          })
          .catch((err) => {
            this.$message.error("当前neo4j网络异常，请稍后再试");
          });
      }
      else if (form.source == "director") {
        this.$axios
          .get("/neo4j/actors/frequent-directors", {
            params: {
              page: this.currentPage,
              per_page: 5,
            }

          })
          .then((res) => {
            console.log(res);
            this.neo4j_speed = res.time;
          })
          .catch((err) => {
            console.log(err);
            this.$message.error("当前neo4j网络异常，请稍后再试");
          });
      }

    },

    echartsInit() {
      //使用时只需要把setOption里的对象换成echarts中的options或者自己的参数即可
      console.log("开始初始化");
      this.$echarts.init(document.getElementById("speed")).setOption({
        title: {
          text: "关系查询耗时对比(s)",
        },
        tooltip: {},
        xAxis: {
          data: ["mysql", "neo4j", "hive"],
        },
        yAxis: {},
        series: [
          {
            name: "查询耗时(s)",
            type: "bar",
            // data: [this.mysql_speed, this.neo4j_speed, this.spark_speed],
            data: [this.mysql_speed, this.neo4j_speed, this.spark_speed],
          },
        ],
      });
    },
  },
};
</script>

<style scoped>
.el-divider--vertical {
  height: 75vh;
}
</style>
