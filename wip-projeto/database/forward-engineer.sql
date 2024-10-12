-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema aplicacao
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema aplicacao
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `aplicacao` DEFAULT CHARACTER SET utf8 ;
USE `aplicacao` ;

-- -----------------------------------------------------
-- Table `aplicacao`.`tiposMensagem`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aplicacao`.`tiposMensagem` (
  `1` INT NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(45) NULL,
  PRIMARY KEY (`1`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aplicacao`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aplicacao`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aplicacao`.`mensagens`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aplicacao`.`mensagens` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_tipo_mensagem` INT NOT NULL,
  `usuarios_id` INT NOT NULL,
  `timestamp_cod` INT NOT NULL,
  `text_msg` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_mensagens_messageType_idx` (`id_tipo_mensagem` ASC) VISIBLE,
  INDEX `fk_mensagens_usuarios1_idx` (`usuarios_id` ASC) VISIBLE,
  CONSTRAINT `fk_mensagens_messageType`
    FOREIGN KEY (`id_tipo_mensagem`)
    REFERENCES `aplicacao`.`tiposMensagem` (`1`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_mensagens_usuarios1`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `aplicacao`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
