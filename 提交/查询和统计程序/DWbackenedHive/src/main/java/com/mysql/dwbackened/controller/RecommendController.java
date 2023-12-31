package com.mysql.dwbackened.controller;


import com.mysql.dwbackened.service.ActorService;
import com.mysql.dwbackened.service.DirectorService;
import com.mysql.dwbackened.service.GenreService;
import com.mysql.dwbackened.service.MovieService;
//import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;

/**
 * @author wyx20
 * @version 1.0
 * @title SuggestController
 * @description
 * @create 2023/12/26 16:49
 */
@RestController
@RequestMapping("/recommend")
public class RecommendController {
//    @Autowired
//    MovieService movieService;
//
//    @Autowired
//    GenreService genreService;
//
//    @Autowired
//    DirectorService directorService;
//
//    @Autowired
//    ActorService actorService;
//
//    @GetMapping("/movie")
////    @ApiOperation(notes="",value="获取输入的电影标题的推荐结果")
//    public HashMap<String,Object> getTitleRecommend(@RequestParam String title,@RequestParam int amount){
//        return movieService.getTitleRecommend(title,amount);
//    }
//
//    @GetMapping("/genre")
////    @ApiOperation(notes="",value="获取输入的电影风格的推荐结果")
//    public HashMap<String,Object> getGenreRecommend(@RequestParam String genre,@RequestParam int amount){
//        return genreService.getGenreRecommend(genre,amount);
//    }
//
//    @GetMapping("/director")
////    @ApiOperation(notes="",value="获取输入的电影导演的推荐结果")
//    public HashMap<String,Object> getDirectorRecommend(@RequestParam String director,@RequestParam int amount){
//        return directorService.getDirectorRecommend(director,amount);
//    }
//
//    @GetMapping("/actor")
////    @ApiOperation(notes="",value="获取输入的电影演员的推荐结果")
//    public HashMap<String,Object> getActorRecommend(@RequestParam String actor,@RequestParam int amount){
//        return actorService.getActorRecommend(actor,amount);
//    }


}
