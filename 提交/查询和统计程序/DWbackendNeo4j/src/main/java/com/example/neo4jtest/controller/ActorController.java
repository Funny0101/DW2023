package com.example.neo4jtest.controller;

import com.example.neo4jtest.dto.*;
import com.example.neo4jtest.service.ActorService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import java.util.List;

@RestController
@RequestMapping("/neo4j/actors") // 可以根据需要调整URL路径
public class ActorController {

    private final ActorService actorService;

    @Autowired
    public ActorController(ActorService actorService) {
        this.actorService = actorService;
    }

    @GetMapping("/frequent-actors")
    public ActorCollaborationResponse getFrequentActors(@RequestParam Integer page, @RequestParam Integer per_page) {
        double startTime = System.currentTimeMillis(); // 获取开始时间
        List<ActorCollaboration> collaborations = actorService.getFrequentCollaborators(page, per_page); // 调用服务方法
        double endTime = System.currentTimeMillis(); // 获取结束时间

        double executionTime = endTime - startTime; // 计算执行时间
        return new ActorCollaborationResponse(collaborations, executionTime/1000.0); // 返回新的封装对象
    }
    @GetMapping("/frequent-actors-number")
    public Integer getFrequentActorsNumber() {
        return actorService.getFrequentCollaboratorNumber();
    }

    @GetMapping("/most-attracted-group-23")
    public Collaboration2and3ResultDTO getCollaboration2and3(String genre) {
        return actorService.getCollaboration2and3(genre);
    }

    @GetMapping("/most-attracted-group-2")
    public Collaboration2ResultDTO getCollaboration2(String genre) {
        return actorService.getCollaboration2(genre);
    }

    @GetMapping("/frequent-directors")
    public ActorDirectorCollaborationResponse getFrequentDirectors(@RequestParam Integer page, @RequestParam Integer per_page) {
        double startTime = System.currentTimeMillis(); // 获取开始时间
        List<ActorDirectorCollaboration> collaborations = actorService.getFrequentDirector(page, per_page); // 调用方法
        long endTime = System.currentTimeMillis(); // 结束时间

        double executionTime = endTime - startTime; // 计算执行时间
        return new ActorDirectorCollaborationResponse(collaborations, executionTime/1000.0); // 返回新的封装对象
    }


}
