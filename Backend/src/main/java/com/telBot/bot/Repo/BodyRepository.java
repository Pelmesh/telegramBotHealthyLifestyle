package com.telBot.bot.Repo;

import com.telBot.bot.model.Body;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface BodyRepository extends JpaRepository<Body, Long> {

    Body findByIdChat(Long idChat);

}
