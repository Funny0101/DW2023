package com.example.neo4jtest.repository;

import com.example.neo4jtest.dto.ActorCollaboration;
import com.example.neo4jtest.dto.ActorDirectorCollaboration;
import com.example.neo4jtest.dto.ActorDoubleCollaboration;
import com.example.neo4jtest.dto.ActorTripleCollaboration;
import com.example.neo4jtest.entity.Actor;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.data.neo4j.repository.Neo4jRepository;
import org.springframework.data.neo4j.repository.query.Query;
import org.springframework.stereotype.Repository;
import java.util.List;

@Repository
public interface ActorRepository extends Neo4jRepository<Actor, Integer> {

    @Query("MATCH (a1:Actor)-[:ACTED]->(:Movie)<-[:ACTED]-(a2:Actor) " +
            "WHERE ID(a1) < ID(a2) " +
            "RETURN a1.actor_name AS actorName1, a2.actor_name AS actorName2, COUNT(*) AS collaborationCount " +
            "ORDER BY collaborationCount DESC " +
            "SKIP ($start - 1) * $perPage " +
            "LIMIT $perPage")
    List<ActorCollaboration> findFrequentCollaborators(int start, int perPage);

    @Query("MATCH (a1:Actor)-[:ACTED]->(:Movie)<-[:ACTED]-(a2:Actor) " +
            "WHERE ID(a1) < ID(a2) " +
            "WITH a1, a2, COUNT(*) AS collaborationCount " +
            "WHERE collaborationCount > 5 " +
            "RETURN COUNT(*) AS frequentCollaborationCount ")
    Integer findFrequentCollaboratorsNum();

    @Query("MATCH (d:Director)-[:DIRECT]->(:Movie)<-[:ACTED]-(a:Actor) " +
            "RETURN a.actor_name as actorName, d.director_name as directorName, COUNT(*) AS collaborationCount " +
            "ORDER BY collaborationCount DESC " +
            "SKIP ($start - 1) * $perPage " +
            "LIMIT $perPage")
    List<ActorDirectorCollaboration> findFrequentDirectors(int start, int perPage);

    @Query("MATCH (a1:Actor)-[:ACTED]->(m:Movie {movie_genre: $genre})<-[:ACTED]-(a2:Actor) " +
            "WHERE ID(a1) < ID(a2) AND m.movie_review_num IS NOT NULL " +
            "RETURN a1.actor_name AS actorName1, a2.actor_name AS actorName2, SUM(COALESCE(TOINTEGER(m.movie_review_num), 0)) AS totalReviews " +
            "ORDER BY totalReviews DESC " +
            "LIMIT 1")
    ActorDoubleCollaboration findMostReviewedCollaboration(String genre);

    @Query("MATCH (a1:Actor)-[:ACTED]->(m1:Movie {movie_genre: $genre})<-[:ACTED]-(a2:Actor)-[:ACTED]->(m2:Movie {movie_genre: $genre})<-[:ACTED]-(a3:Actor) " +
            "WHERE ID(a1) < ID(a2) AND ID(a2) < ID(a3) AND m1.movie_review_num IS NOT NULL AND m2.movie_review_num IS NOT NULL " +
            "RETURN a1.actor_name AS actorName1, a2.actor_name AS actorName2, a3.actor_name AS actorName3, SUM(COALESCE(TOINTEGER(m1.movie_review_num), 0) + COALESCE(TOINTEGER(m2.movie_review_num), 0)) AS totalReviews " +
            "ORDER BY totalReviews DESC " +
            "LIMIT 1")
    ActorTripleCollaboration findMostReviewedTripleCollaboration(String genre);





}
