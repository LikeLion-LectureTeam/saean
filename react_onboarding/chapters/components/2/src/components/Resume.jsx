export default function Resume(props) {
    return (
        <div>
            <h1>{props.hello}</h1>
            <p>이름: {props.name}</p>
            <p>취미: {props.hobby}</p>
            <p>좋아하는 음식: {props.food}</p>
            <p>좋아하는 색: {props.color}</p>
        </div>
    );
}
