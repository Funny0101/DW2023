package com.example.neo4jtest.service;

import com.example.neo4jtest.dto.*;
import com.example.neo4jtest.repository.ActorRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class ActorService {

    @Autowired
    private ActorRepository actorRepository;

    public List<ActorCollaboration> getFrequentCollaborators(Integer start, Integer perPage) {
        return actorRepository.findFrequentCollaborators(start, perPage);
    }
    public List<ActorDirectorCollaboration> getFrequentDirector(Integer start, Integer perPage) {
        return actorRepository.findFrequentDirectors(start, perPage);
    }

    public Integer getFrequentCollaboratorNumber() {
        return actorRepository.findFrequentCollaboratorsNum();
    }

    public Collaboration2and3ResultDTO getCollaboration2and3(String genre) {
        double startTime = System.currentTimeMillis(); // 获取开始时间

        ActorDoubleCollaboration doubleCollab = actorRepository.findMostReviewedCollaboration(genre);
        ActorTripleCollaboration tripleCollab = actorRepository.findMostReviewedTripleCollaboration(genre);

        double endTime = System.currentTimeMillis(); // 结束时间

        double executionTimeInSeconds = (endTime - startTime) / 1000.0; // 将纳秒转换为秒

        return new Collaboration2and3ResultDTO(doubleCollab, tripleCollab, executionTimeInSeconds);
    }

    public Collaboration2ResultDTO getCollaboration2(String genre) {
        double startTime = System.currentTimeMillis(); // 获取开始时间

        ActorDoubleCollaboration doubleCollab = actorRepository.findMostReviewedCollaboration(genre);

        double endTime = System.currentTimeMillis(); // 结束时间

        double executionTimeInSeconds = (endTime - startTime) / 1000.0;

        return new Collaboration2ResultDTO(doubleCollab, executionTimeInSeconds);
    }

}
