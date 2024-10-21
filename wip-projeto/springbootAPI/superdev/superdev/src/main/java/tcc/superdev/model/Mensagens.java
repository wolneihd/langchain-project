package tcc.superdev.model;

import javax.persistence.Column;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Entity;
import javax.persistence.Table;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;

@Entity
@Table(name = "mensagens")
public class Mensagens {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "id_tipo_mensagem")
    private TiposMensagem tiposMensagem;

    @ManyToOne
    @JoinColumn(name = "usuarios_id")
    private Usuarios usuarios;

    private Long timestampCod;

    @Column(length = 255, nullable = false)
    private String textMsg;

    // Getters e Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public TiposMensagem getTiposMensagem() {
        return tiposMensagem;
    }

    public void setTiposMensagem(TiposMensagem tiposMensagem) {
        this.tiposMensagem = tiposMensagem;
    }

    public Usuarios getUsuarios() {
        return usuarios;
    }

    public void setUsuarios(Usuarios usuarios) {
        this.usuarios = usuarios;
    }

    public Long getTimestampCod() {
        return timestampCod;
    }

    public void setTimestampCod(Long timestampCod) {
        this.timestampCod = timestampCod;
    }

    public String getTextMsg() {
        return textMsg;
    }

    public void setTextMsg(String textMsg) {
        this.textMsg = textMsg;
    }
}
